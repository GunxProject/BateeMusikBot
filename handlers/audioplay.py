# this module i created only for playing music using audio file, idk, because the audio player on play.py module not working
# so this is the alternative
# audio play function
# tede ganteng tq

from os import path

import converter
from callsmusic import callsmusic, queues
from config import (
    AUD_IMG,
    BOT_USERNAME,
    DURATION_LIMIT,
    GROUP_SUPPORT,
    QUE_IMG,
    UPDATES_CHANNEL,
)
from handlers.play import convert_seconds
from helpers.filters import command, other_filters
from helpers.gets import get_file_name
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["psound", f"psound@{BOT_USERNAME}"]) & other_filters)
async def stream(_, message: Message):
    costumer = message.from_user.mention
    lel = await message.reply_text("🔁 **Sedang Memproses** file dahulu...")

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Group Batak", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="Channel Batak", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    audio = message.reply_to_message.audio if message.reply_to_message else None
    if not audio:
        return await lel.edit("💭 **Tolong balas ke file audio telegram**")
    if round(audio.duration / 60) > DURATION_LIMIT:
        return await lel.edit(
            f"❌ **Musik dengan durasi lebih dari** `{DURATION_LIMIT}` **menit, tidak dapat diputar !**"
        )

    # tede_ganteng = True
    title = audio.title
    file_name = get_file_name(audio)
    duration = convert_seconds(audio.duration)
    file_path = await converter.convert(
        (await message.reply_to_message.download(file_name))
        if not path.isfile(path.join("downloads", file_name))
        else file_name
    )
    # ambil aja bg
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
            photo=f"{QUE_IMG}",
            caption=f"💡 **Musik ditambahkan ke antrean »** `{position}`\n\n🏷 **Judul :** {title[:50]}\n⏱ **Durasi :** `{duration}`\n🎧 **Permintaan dari :** {costumer}",
            reply_markup=keyboard,
        )
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
            photo=f"{AUD_IMG}",
            caption=f"🏷 **Judul :** {title[:50]}\n⏱ **Durasi :** `{duration}`\n💡 **Status:** `Diputar`\n"
            + f"🎧 **Permintaan dari :** {costumer}",
            reply_markup=keyboard,
        )

    return await lel.delete()

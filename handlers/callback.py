# (C) 2021 VeezMusic-Project

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Horas [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) memungkinkan anda untuk dapat memutar musik di grup atau channel anda melalui obrolan suara Telegram !**

💡 **Cari tahu semua perintah bot dan cara kerjanya dengan mengklik tombol » 📚 Perintah dibawah !**

❔ **Untuk mengetahui cara menggunakan bot ini, silakan klik tombol » ❓ Cara Kerja dibawah !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("📚 Perintah - Perintah", callback_data="cbcmds")],
                [
                    InlineKeyboardButton("❓ Cara Kerja", callback_data="cbhowtouse"),
                    InlineKeyboardButton("💝 Donasi", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grup Batak", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📢 Channel Batak", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🤵 Pemilik Saya", url="https://t.me/galang109"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Halo** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **Tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

» **CMD = Perintah**

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 CMD Dasar", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 CMD Lanjutan", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 CMD Admin", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 CMD Sudo", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 CMD Pemilik", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah dasar**

🎧 [ Perintah Untuk Di Grup ]

/batee (Judul Lagu) - Putar lagu dari youtube.
/ytp (Judul Lagu) - Putar lagu langsung dari youtube tanpa pemilihan.
/vplay (balas audio) - Putar lagu menggunakan file audio.
/playlist - Tampilkan daftar lagu dalam antrian.
/song (nama lagu) - Download lagu dari youtube.
/search (nama video) - Cari info video dari youtube.
/vsong (nama video) - Download video dari youtube.
/lyric (nama lagu) - Cari lirik lagu.

🎧 [ Perintah Untuk Di Channel ]

/cbatee - Putarkan lagu di obrolan suara channel anda.
/cplayer - Tampilkan lagu yang sedang di putar.
/cpause - Jeda lagu yang sedang di putar.
/cresume - Lanjutkan lagu yang dijeda.
/cskip - Lompat ke lagu berikutnya.
/cends - Akhiri pemutaran lagu.
/refresh - Segarkan cache admin.
/ubjoinc - Mengundang asisten untuk bergabung ke channel Anda.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah lanjutan**

/start (dalam grup) - Melihat status bot hidup.
/reload - Muat ulang bot dan segarkan daftar admin.
/ping - Periksa status ping bot.
/uptime - Periksa status waktu aktif bot.
/id - Tunjukkan grup/id pengguna & lainnya.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah khusus admin**

/player - Tampilkan status pemutaran musik.
/pause - Jeda lagu yang diputar.
/resume - Lanjutkan lagu yang dijeda.
/skip - Melompat ke lagu berikutnya.
/ends - Hentikan Pemutaran Lagu.
/join - Mengundang asisten bergabung ke grup Anda.
/getout - Perintahkan asisten untuk keluar dari grup anda.
/auths - Memberikan wewenang/ijin ke seseorang untuk menggunakan perintah admin.
/unauths - Membatalkan wewenang/ijin ke seseorang yg sebelumnya di beri ijin untuk menggunakan perintah admin.
/control - Buka panel pengaturan pemutaran lagu.
/delcmd (on | off) - Aktifkan / nonaktifkan fitur del cmd.
/music (on / off) - Nonaktifkan / aktifkan bot di grup Anda.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah untuk sudo akun**

/leaveall - Perintahkan asisten untuk pergi dari semua grup.
/stats - Memperlihatkan statistik bot.
/rmd - Hapus semua file yang diunduh.
/eval (pertanyaan) - Mengeksekusi kode.
/sh (pertanyaan) - Menjalankan kode.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah untuk pemilik**

/stats - Memperlihatkan statistik bot.
/broadcast (membalas pesan) - Mengirim pesan siaran dari bot.
/block (id pengguna - durasi - alasan) - Blokir pengguna untuk menggunakan bot.
/unblock (id pengguna - alasan) - Buka blokir pengguna yang Anda blokir untuk menggunakan bot.
/blocklist - Memperlihatkan daftar pengguna yang diblokir untuk menggunakan bot.

📝 Note: Semua perintah yang dimiliki bot ini dapat dijalankan oleh pemilik bot tanpa terkecuali.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **CARA MENGGUNAKAN BOT INI :**

1.) **Pertama, tambahkan bot ini ke grup Anda.**
2.) **Kemudian jadikan bot ini sebagai admin dan berikan semua izin kecuali admin anonim.**
3.) **Tambahkan @{ASSISTANT_NAME} ke grup anda atau ketik perintah /join di grup anda untuk mengundangnya.**
4.) **Buka/hidupkan obrolan suara terlebih dahulu sebelum mulai memutar musik.**
5.) **Berikan perintah /batee (judul lagu).

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Daftar Perintah", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Tutup", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 Berikut adalah menu kontrol bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Tutup", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 **Berikut adalah informasi fitur :**
        
**💡 Fitur :** Hapus setiap perintah yang dikirim oleh pengguna untuk menghindari spam di grup !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Halo** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **Tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

» *CMD = Perintah**

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 CMD Dasar", callback_data="cblocal"),
                    InlineKeyboardButton("📕 CMD Lanjutan", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("📘 CMD Admin", callback_data="cblamp"),
                    InlineKeyboardButton("📗 CMD Sudo", callback_data="cblab"),
                ],
                [InlineKeyboardButton("📙 CMD Owner", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **CARA MENGGUNAKAN BOT INI :**

1.) **Pertama, tambahkan bot ini ke grup Anda.**
2.) **Kemudian jadikan bot ini sebagai admin dan berikan semua izin kecuali admin anonim.**
3.) **Tambahkan @{ASSISTANT_NAME} ke grup anda atau ketik perintah /join di grup anda untuk mengundangnya.**
4.) **Buka/hidupkan obrolan suara terlebih dahulu sebelum mulai memutar musik.**
5.) **Berikan perintah /batee (judul lagu).

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah dasar**

🎧 [ Perintah Untuk Di Grup ]

/batee (Judul Lagu) - Putar lagu dari youtube.
/ytp (Judul Lagu) - Putar lagu langsung dari youtube tanpa pemilihan.
/vplay (balas audio) - Putar lagu menggunakan file audio.
/playlist - Tampilkan daftar lagu dalam antrian.
/song (nama lagu) - Download lagu dari youtube.
/search (nama video) - Cari info video dari youtube.
/vsong (nama video) - Download video dari youtube.
/lyric (nama lagu) - Cari lirik lagu.

🎧 [ Perintah Untuk Di Channel ]

/cbatee - Putarkan lagu di obrolan suara channel anda.
/cplayer - Tampilkan lagu yang sedang di putar.
/cpause - Jeda lagu yang sedang di putar.
/cresume - Lanjutkan lagu yang dijeda.
/cskip - Lompat ke lagu berikutnya.
/cends - Akhiri pemutaran lagu.
/refresh - Segarkan cache admin.
/ubjoinc - Mengundang asisten untuk bergabung ke channel Anda.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah lanjutan**

/start (dalam grup) - Melihat status bot hidup.
/reload - Muat ulang bot dan segarkan daftar admin.
/ping - Periksa status ping bot.
/uptime - Periksa status waktu aktif bot.
/id - Tunjukkan grup/id pengguna & lainnya.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah khusus admin**

/player - Tampilkan status pemutaran musik.
/pause - Jeda lagu yang diputar.
/resume - Lanjutkan lagu yang dijeda.
/skip - Melompat ke lagu berikutnya.
/ends - Hentikan Pemutaran Lagu.
/join - Mengundang asisten bergabung ke grup Anda.
/getout - Perintahkan asisten untuk keluar dari grup anda.
/auths - Memberikan wewenang/ijin ke seseorang untuk menggunakan perintah admin.
/unauths - Membatalkan wewenang/ijin ke seseorang yg sebelumnya di beri ijin untuk menggunakan perintah admin.
/control - Buka panel pengaturan pemutaran lagu.
/delcmd (on | off) - Aktifkan / nonaktifkan fitur del cmd.
/music (on / off) - Nonaktifkan / aktifkan bot di grup Anda.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah untuk sudo akun**

/leaveall - Perintahkan asisten untuk pergi dari semua grup.
/stats - Memperlihatkan statistik bot.
/rmd - Hapus semua file yang diunduh.
/eval (pertanyaan) - Mengeksekusi kode.
/sh (pertanyaan) - Menjalankan kode.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Berikut adalah perintah untuk pemilik**

/stats - Memperlihatkan statistik bot.
/broadcast (membalas pesan) - Mengirim pesan siaran dari bot.
/block (id pengguna - durasi - alasan) - Blokir pengguna untuk menggunakan bot.
/unblock (id pengguna - alasan) - Buka blokir pengguna yang Anda blokir untuk menggunakan bot.
/blocklist - Memperlihatkan daftar pengguna yang diblokir untuk menggunakan bot.

📝 Note: Semua perintah yang dimiliki bot ini dapat dijalankan oleh pemilik bot tanpa terkecuali.

⚡ __Dipersembahkan oleh {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )

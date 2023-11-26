import pywhatkit as kit

# Nomor penerima (dengan kode negara, tanpa tanda +)
nomor_penerima = "+6281222518720"  # Ganti dengan nomor penerima sesuai kebutuhan
pesan = "Halo, ini pesan dari Python!"

# Waktu pengiriman (format: jam dan menit)
jam = 21  # Jam (24 jam)
menit = 54  # Menit

# Kirim pesan WhatsApp
kit.sendwhatmsg(nomor_penerima, pesan, jam, menit)

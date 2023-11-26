# format string

# contoh generic
# String
nama = "adrian"
format_str = f"Hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

# Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"Bilangan bulat = {angka:d}"
# ":d" disamping mengartikan bahwa angka tersebut adalah bilangan bulat
# sebenarnya tidak masalah jika tidak memakai ":d" tersebut
print(format_str)

# bilangan ribuan
angka = 2000
format_str = f"Ribuan = {angka:,}"  # dia akan menjadi "2,000"
print(format_str)

# bilangan Jutaan
angka = 2000000
format_str = f"Jutaan = {angka:,}"  # dia akan menjadi "2,000,000"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"Desimal = {angka:.2f}"
# Titik (.) untuk menandakan angka di belakang desimalnya "2005."
# 2 untuk menandakan berapa angka yang akan di outputkan
# f untuk menandakan tipe data nya adalah FLOAT, jika ada koma-komaan atau titik
print(format_str)

# Menampilkan leading zero
angka = 2005.54321
format_str = f"Desimal = {angka:08.1f}"
# 0 Untuk menambahkan angka 0 didepannya menjadi "02005.543"
# 8 adalah total angkanya yang artinya nanti akan menjadi "2005.543"
# Titik (.) untuk menandakan angka di belakang desimalnya "2005."
# 2 untuk menandakan berapa angka yang akan di outputkan
# f untuk menandakan tipe data nya adalah FLOAT, jika ada koma-komaan atau titik
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10.341
angka_plus = 10.9456
format_minus = f"Minus = {angka_minus:-.2f}"
format_plus = f"Plus = {angka_plus:+.1f}"
# tanda (+) untuk mengoutputkan tanda (+) di angka 10
print(format_minus)
print(format_plus)

# mengformat persen
persentase = 0.045
format_persen = f"Persen = {persentase:.3%}"
# tanda (%) untuk menambahkan persen di belakangnya
# ".3" untuk menambahkan 3 angka dibelakang koma
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
jumlah_string = f"Harga total = {harga*jumlah:,}"
print(jumlah_string)

# format angka lain (binary,octal dan hexadecimal)
angka = 225
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal  = {oct(angka)}"
format_hex = f"Hex    = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)

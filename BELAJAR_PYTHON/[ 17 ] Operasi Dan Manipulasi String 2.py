# Operator Dalam bentuk methods

# Merubah case dari string

# Merubah semua ke upper case (menjadi huruf besar semua)

data1 = "Bro!"
print("Normal = ", data1)

data1 = data1.upper()
print("Upper = ", data1)

# Merubah semua ke lower case (menjadi huruf kecil semua)
data2 = "Gua mEmangg KeRenzz"
print("Normal = ", data2)

data2 = data2.lower()
print("Lower = ", data2)

# Pengecekan dengan IsX Method

# contoh pengecekan lower case
data3 = "brader"
apakah_upper = data3.isupper()  # Tipe datanya Boolean!
print(data3, "Is Upper ? :", apakah_upper)
apakah_lower = data3.islower()  # Tipe datanya Boolean!
print(data3, "Is Lower ? :", apakah_lower)

# isAlpha untuk mengecek semuanya adalah huruf
data4 = "AdrianMusa"
apakah_alpha = data4.isalpha()
print(data4, "Is Alpha ? :", apakah_alpha)

# isAlnum huruf dan angka/numerik seperti yang ada biasanya di password
data5 = "adrianmusa3434"
apakah_alnum = data5.isalnum()
print(data5, "Is Alnum ? :", apakah_alnum)

# isDecimal untuk mengecek komponennya hanyalah angka
data6 = "3434"
apakah_decimal = data6.isdecimal()
print(data6, "Is decimal ? :", apakah_decimal)

# isSpace untuk mengecek string kosong seperti (spasi,tab, newline (\n))
data7 = " \n "
apakah_space = data7.isspace()
print(data7, "Is space ? :", apakah_space)

# isTitle semua kata dimulai dengan huruf besar dan tidak boleh ada simbol lainnya!
data8 = " Adrian Adalah Seorang Programmer "
apakah_title = data8.istitle()
print(data8, "Is title ? :", apakah_title)

# Mengecek Komponen startwith() endswith()
cekawal = "Gua adalah seorang Programmer".startswith("Gua")  # Diambil dari awal kata
print("Data Awal :", cekawal)
# Mengecek Komponen endswith()
cekakhir = "Gua adalah seorang Programmer".endswith(
    "Programmer"
)  # Diambil dari  akhir kata
print("Data Akhir :", cekakhir)

# Penggabungan komponen join()
pisah = ["gua", "adalah", "programmer"]
gabung = ",".join(pisah)
print("Hasil Pisah :", pisah)
print("Hasil Gabungan :", gabung)

gabung2 = " ".join(pisah)
print("Hasil Gabungan :", gabung2)

gabung3 = " _ ".join(pisah)
print("Hasilnya : ", gabung3)

# Penggabungan komponen split()
nama = "adrianYesmusaYesalfauzan"
print("Hasilnya : ", nama.split("Yes"))  # "Yes" --> hasilnya akan hilang

# Alokasi karakter rjust()
print(5 * "=", "CONTOH", "=" * 5)  # ini terlalu lama
kanan = "kanan".rjust(10)
print("=", kanan, "=")

# Alokasi karakter ljust()
kiri = "kiri".ljust(10)
print("=", kiri, "=")

# Alokasi karakter center()
center = "center".center(10, "+")
print("=", center, "=")

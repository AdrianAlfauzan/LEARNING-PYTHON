import os

os.system("cls")

print(3 * "=", "Membaca file txt", 3 * "=")

# [+] mode --> menentukan buka data ini sebagai apa? apakah read,write dll
# [+] mode = "r" --> read
# [+] mode = "w" --> write

file = open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 64 ] Read External file - Open dan With\data.txt",
    mode="r",
)
# readable --> untuk mengecek apakah bisa di baca atau tidak
print(
    f"Status File apakah bisa di baca atau tidak ? (True or False) : {file.readable()}"
)
print(
    f"Status File apakah bisa di write atau tidak ? (True or False) : {file.writable}"
)

# [+] Read adalah sebuah method
# [+] read --> membaca seluruh isi di dalam file
# print(file.read())

# [+] readline --> print file, jadi dia ini baris per baris / berurutan
# [+] readline --> membaca seluruh isi file dalam baris per baris
# [+] baca baris pertama
# print(file.readline(), end="")
# [+] baca baris kedua
# print(file.readline(), end="")
# [+] baca baris ketiga
# print(file.readline(), end="")
# untuk menghilangkan tanda "\n" pakai --> end= "" --> jadi dia mendelete

# [+] readlines --> membaca seluruh isi dalam file dalam sebuah list
# print(file.readlines())


# PROBLEM NYA : SETIAP HABIS OPEN, KITA HARUS TUTUP.
print(f"Apakah file sudah di close ? (True or False) : {file.closed}")
file.close()  # ini method untuk menutup filenya
print(f"Apakah file sudah di close ? (True or False) : {file.closed}")


# Salah satu teknik membuka file di python yang SIMPLE!!! :
print("\n", 3 * "=", "Membaca file txt dgn with", 3 * "=")
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 64 ] Read External file - Open dan With\data.txt",
    mode="r",
) as file:  # dengan saat ini dibuka, apa yang akan kita lakukan ?
    content = file.readline()
    print(content, end="")
print(f"Apakah file sudah di close ? (True or False) : {file.closed}")

# Lambda Function --> bisa membuat program kita lebih simple
import os

os.system("cls")


def f_kuadrat(angka):
    return angka**2


print(f"Hasil fungsi kuadrat = {f_kuadrat(3)}")

# Kita coba dengan lambda agar lebih simple
# variabel_output = lambda argument: expression
lambda_kuadrat = lambda angka: angka**2
print(f"Hasil lambda kuadrat = {lambda_kuadrat(5)}")

# lambda 2 input
pangkat = lambda num, pow: num**pow
print(f"Hasil lambda pangkat = {pangkat(4,2)}")


# Kegunaannya lambda apa sih?

# 1. untuk sorting list biasa
data_list = ["adrian", "leon", "prince"]
data_list.sort()
print(f"sorted list = {data_list}")

# 2. kita mau sorting dia pakai panjang
data_list.sort(key=len)
print(f"sorted list by len = {data_list}")


# 3. kita mau sorting dia pakai panjang
# MENGGUNAKAN FUNGSI
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=len)
print(f"sorted list by len = {data_list}")


# 4. kita mau sorting dia pakai panjang
# MENGGUNAKAN LAMBDA
data_list = ["adrian", "leon11", "prince"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# Menggunakan fungsi
def kurang_dari_lima(angka):
    return angka < 5


data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(f"angka filter dgn fungsi = {data_angka_baru}")

# Menggunakan lambda
data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(f"angka filter dgn lambda = {data_angka_baru}")

# kasus genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(f"Data genap dengan lambda = {data_genap}")

# kasus ganjil
data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(f"Data ganjil dengan lambda = {data_ganjil}")

# Kasus Kelipatan 3
data_kelipatan_3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(f"Data kelipatan 3 dengan lambda = {data_kelipatan_3}")


# Anonymous function
# currying --> ini dari haskell curry, dia yang bikin bahasa haskell
# dia membuat tehnik ini dgn lambda


def pangkat(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat(5, 2)
print(f"fungsi biasa = {data_hasil}")


# dengan currying menjadi
def pangkat(n):
    return lambda angka: angka**n


hasil_n = pangkat(6)
pangkat6 = hasil_n
print(f"pangkat 6 = {pangkat6(2)} ")

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")

print(f"pangkat bebas = {pangkat(4)(5)}")

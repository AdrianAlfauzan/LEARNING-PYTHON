# Import

# Fungsinya adalah untuk mengambil program dari file external .py


import ProgramPrint
import Main_App

# --> kita memanggil file yang ada diluar

# Spesifikasinya :
# 1. Berfungsi untuk menyambung program dari external
# 2. Import dengan data

# Cluenya adalah apa saja yang ada di dalam module, kita tinggal panggil isinya

import Data_Data

# Data ada di namespace Data_Data
print(Data_Data.data)
print(Data_Data.input_data)

import data_lagi

print(data_lagi.data)
# pemanggilannya double/ada yang sama tapi outputnya beda, itulah fungsinya!

# Import dengan fungsi
import matematika

# bisa menggunakan cara 1
# print(matematika.tambah(50, 50))

# bisa menggunakan cara 2
hasil = matematika.tambah(10, 10)
print(hasil)

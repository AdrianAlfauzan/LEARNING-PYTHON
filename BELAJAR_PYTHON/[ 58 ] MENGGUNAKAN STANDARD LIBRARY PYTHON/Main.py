import datetime

data_waktu = datetime.datetime.now()
print(f"Datetime Now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Tanggal : {data_waktu.day}")  # day ini untuk tanggal
print(f"Hari : {data_waktu.strftime('%A')}")

from collections import Counter

# Collections --> kumpulan" data seperti array, list dll
# Counter --> untuk menghitung jumlah member
data = ["a", "b", "c", "d", "e", "a","d","d","d"]
data_count = Counter(data)
print(f"Jumlah Data : {data_count}")
print(f"Jumlah Data a : {data_count["a"]}")
print(f"Jumlah Data d : {data_count["d"]}")

# atau pakai cara bawah

import io
import os

# Menetapkan direktori kerja saat ini ke direktori skrip
os.chdir(os.path.dirname(__file__))

# Menggunakan path relatif ke file
file_path = "file_text.txt"

with io.open(file_path, "r") as file:
    print(file.read())



# 1. Mode write

# dia ini akan membuat file baru jika tidak ada, lalu
# akan menimpa atau overwrite isinya

# encoding --> agar jelas character" nya dengan uts-8
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_1.txt",
    "w",
    encoding="utf-8",
) as file:
    file.write("Halo Programmer")
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_1.txt",
    "w",
    encoding="utf-8",
) as file:
    file.write("Halo Programmer 1")
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_1.txt",
    "w",
    encoding="utf-8",
) as file:
    file.write("OVER WRITE")


"""Bagaimana cara menambahkan di bawahnya?"""
# 2. Mode append
# untuk pakai append cukup dengan --> mode="a" atau langsung "a"
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_2.txt",
    "w",
    encoding="utf-8",
) as file:
    file.write("Halo Programmer 45 \n")
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_2.txt",
    "a",
    encoding="utf-8",
) as file:
    file.write("Halo Programmer 100 \n")
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_2.txt",
    "a",
    encoding="utf-8",
) as file:
    file.write("Menambah dengan append")

# 3. Mode r+
# dia akan menimpa.
with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_3.txt",
    "w",
    encoding="utf-8",
) as file:
    file.write("data ke 3\n")

with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_3.txt",
    "r+",
    encoding="utf-8",
) as file:
    file.write("Baris - 1 \n")
    file.write("Baris - 2 \n")
    file.write("Baris - 3 \n")

with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_3.txt",
    "r+",
    encoding="utf-8",
) as file:
    data = file.read()
    print(data)

with open(
    "D:\BELAJAR FT MY CODING\BELAJAR PYTHON\BELAJAR_PYTHON\[ 65 ] Write External File\data_3.txt",
    "r+",
    encoding="utf-8",
) as file:
    file.write("Adrian")
    # ini akan menimpa di file .txt pada baris pertama.
    # dia akan buka lalu akan menimpa sesuai panjang data.

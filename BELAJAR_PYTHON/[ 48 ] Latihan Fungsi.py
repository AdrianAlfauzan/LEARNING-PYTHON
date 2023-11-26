"""Latihan fungsi"""

import os

# Program menghitung luas dan keliling persegi panjang

# CONTOH
# Membuat header program
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai Panjang : "))

# # Program menghitung luas

# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # Tampilkan hasil
# print(f"Hasil perhitungan LUAS = {LUAS}")
# print(f"Hasil perhitungan KELILING = {KELILING}")


def header():
    """Fungsi Header"""
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")


def input_user():
    """Fungsi Input User"""
    # Mengambil input user
    LEBAR = int(input("Masukkan nilai lebar : "))
    PANJANG = int(input("Masukkan nilai Panjang : "))

    return LEBAR, PANJANG


def hitung_luas(lebar, panjang):
    """Fungsi Luas"""
    return lebar * panjang


def hitung_keliling(lebar, panjang):
    """Fungsi Keliling"""
    return 2 * (lebar + panjang)


def display(message, value):
    """Fungsi Display"""
    print(f" Hasil Perhitungan {message} {value}")


# Program utamanya
while True:
    header()
    # opsi = input("Pilih 1 untuk luas")
    iniLEBAR, iniPANJANG = input_user()
    LUAS = hitung_luas(iniLEBAR, iniPANJANG)
    KELILING = hitung_keliling(iniLEBAR, iniPANJANG)
    display("Luas :", LUAS)
    display("Keliling :", KELILING)

    ApakahLanjut = str(input("Lanjut (y/n)? "))
    if ApakahLanjut == "n" or ApakahLanjut == "N":
        print("Program Berhenti!")
        break
    elif ApakahLanjut == "y" or ApakahLanjut == "Y":
        continue
    else:
        print("inputan salah!")
        break

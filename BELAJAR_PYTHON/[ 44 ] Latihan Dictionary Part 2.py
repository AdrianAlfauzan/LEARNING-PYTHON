import datetime
import os
import string
import random

# Fromkeys

# Template Dict Mahasiswa
mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111, 1, 11),
}
data_mahasiswa = {}
# Template Dict Mahasiswa

while True:
    # MEMBUAT BAGIAN ATAS KOSONG DENGAN SENDIRINYA
    os.system("cls")  # UNTUK WINDOWS
    # os.system("clear")  # UNTUK LINUX / Mac OS
    # MEMBUAT BAGIAN ATAS KOSONG DENGAN SENDIRINYA

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    print(mahasiswa)

    mahasiswa["nama"] = input("Nama Mahasiswa : ")
    mahasiswa["nim"] = input("nim Mahasiswa : ")
    mahasiswa["sks_lulus"] = int(input("sks_lulus Mahasiswa : "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("tanggal lahir (1-31): "))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
    print(mahasiswa)

    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(4)))
    data_mahasiswa.update({KEY: mahasiswa})

    # CODE DIBAWAH ADA DI MATERI FILE SEBELUMNYA
    print(f"{'KEY' :<6} {'nama': <17} {'NIM':<8} {'SKS':^10} {'Lahir':^10}")
    print("-" * 50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
        print(f"{KEY :<6} {NAMA: <17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

    print("\n")
    apakah_selesai = input("Apakah ingin lanjut? (y/n) ?")
    if apakah_selesai == "n":
        break
    print("PROGRAM SELESAI!")

import datetime
import os

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

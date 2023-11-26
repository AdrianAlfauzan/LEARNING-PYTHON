import os  # untuk hapus di atasnya


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
    opsi = input(
        "Pilih 1 untuk luas \nPilih 2 untuk Keliling \nPilih 3 untuk keduanya \nOpsi :"
    )
    if opsi == "1":
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("Luas :", LUAS)
    elif opsi == "2":
        LEBAR, PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("Keliling :", KELILING)
    elif opsi == "3":
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("Luas :", LUAS)
        display("Keliling :", KELILING)
    else:
        print("Tidak ada opsi yang tertera!")

    ApakahLanjut = str(input("Lanjut (y/n)? "))
    if ApakahLanjut == "n" or ApakahLanjut == "N":
        print("Program Berhenti!")
        break
    elif ApakahLanjut == "y" or ApakahLanjut == "Y":
        continue
    else:
        print("inputan salah!")
        break

"Fungsi dengan argumen (input)"

"""def nama_fungsi(parameter):
    # badan fungsi
"""


def hello_world(nama):
    """Fungsi hello world menerima input dengan variabel nama"""
    print(f"Selamat datang dunia wahai {nama}")


hello_world("Adrian")
hello_world("Ronaldo")

# Program tambah


def tambah(angka_1, angka_2):
    """fungsi tambah"""
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")


tambah(1, 5)
tambah(10, 50)


def say_hi(list_peserta):
    """ini adalah fungsi say hi"""
    # list_peserta[2] = "kaka"
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")


anggota_boyband = ["adrian", "ronaldo", "pessi"]
say_hi(anggota_boyband)

# print(anggota_boyband[2])

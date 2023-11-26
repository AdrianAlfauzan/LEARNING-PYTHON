"""Default Argument"""

# Ini normal syntaxnya
# def fungsi (argument/paraemeter):


# bagaimana jika kita tidak mencantumkan nilai argumentnya? berarti harus ada nilai defaultnya!
# contoh :
# def fungsi (argument = nilai defaultnya):


# contoh 1
print("contoh 1")


def say_hello(nama="Ganteng"):
    """Fungsi dengan default argument"""
    print(f"Hallo {nama}")


say_hello("Adrian")
say_hello()


# contoh 2
print("\n contoh 2")


def sapa_dia(nama, pesan="Apa kabar?"):
    """Fungsi dengan satu input biasa dan satu default argument"""
    print(f"hai {nama}, {pesan}")


sapa_dia("Ronaldo", "Hai ganteng")
sapa_dia("Pessiun")


# contoh 3
print("\n contoh 3")


def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil


print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(angka=5, pangkat=2)
print(hasil)


# contoh 4
print("\n contoh 4")


def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil


print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(angka=5, pangkat=3)
print(hasil)

# contoh 5
print("\n contoh 5")


def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil


print(fungsi())
print(fungsi(input3=10))

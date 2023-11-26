import os

os.system("cls")


def userinput():
    print(
        """Ketik 1 untuk Opsi kali = * 
        \nKetik 2 untuk Opsi bagi = / 
        \nKetik 3 untuk Opsi tambah = + 
        \nKetik 4 untuk Opsi kurang = -
        """
    )
    opsi = input("Masukkan opsinya : ")
    input1 = int(input("Masukkan input ke 1 :"))
    input2 = int(input("Masukkan input ke 2 :"))
    return opsi, input1, input2


def hitung_kalkulator(opsi, input1, input2):
    if opsi == "1":
        return iniInput1 * iniInput2
    elif opsi == "2":
        return iniInput1 / iniInput2
    elif opsi == "3":
        return iniInput1 + iniInput2
    elif opsi == "4":
        return iniInput1 - iniInput2
    else:
        return "tidak ada opsi tertera"


while True:
    opsi, iniInput1, iniInput2 = userinput()
    hasil = hitung_kalkulator(opsi, iniInput1, iniInput2)
    print("hasil : ", hasil)

    Lanjut = str(input("Apakah mau lanjut? y/n : "))
    if Lanjut == "n":
        print("Berhenti!")
        break

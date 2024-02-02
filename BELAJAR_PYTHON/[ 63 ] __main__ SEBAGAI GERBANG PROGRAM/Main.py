# __main__ ini adalah top level code environment

# __name__ = "__main__" --> ini akan terjadi jika ada di file program utama

# __name__ pada file program utama
print(f"Nilai __name__ main.py = {__name__}")

# __name__ pada file program file eksternal
import fungsi

# --> outputnya akan "Nilai __name__ fungsi.py = fungsi"


"""Jadi rulesnya adalah __name__ ini akan berubah menjadi __main__ saat kita panggil 
sebagai program utama."""


# contoh penggunaan __main__


# deklarasi
def fungsi_tambah(a: int, b: int) -> int:
    return a + b


# fungsi utama wajib pakai "__name__"
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f"Hasil tambah = {hasil}")
else:
    print("Program bukanlah __main__ / bukan program utama!")

# ini contoh BUKAN fungsi utama
if __builtins__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f"Hasil tambah = {hasil}")
else:
    print("Program bukanlah __main__ / bukan program utama!")


# import packagenya
import package

# ini tidak akan terjadi apa - apa
# akan tetapi jika di panggil di cmd dengan "python package" dia akan keluar hasilnya
# ini sama seperti di cmd jika kita mengetik "python -m venv"

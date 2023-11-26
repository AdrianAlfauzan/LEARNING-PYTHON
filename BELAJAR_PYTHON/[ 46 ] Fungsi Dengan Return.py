import os

os.system("cls")
# di atas ini hanya untuk menghapus sesuatu di atas terminal

"""Fungsi dengan kembalian"""
# Template fungsi dengan kembalian
# def nama_fungsi(parameter/argumen):
#           badan fungsi
#           return output


# fungsi kuadrat
def kuadrat(input_angka):
    """fungsi kuadrat"""
    output_kuadrat = input_angka**2
    return output_kuadrat


# cara output 1
y = kuadrat(3)
print(y)
# cara output 1

# cara output 2
# x = kuadrat(6)
# print(x)
# atau pakai cara...
print(kuadrat(6))
# cara output 2

# cara output 3
z = 10 + kuadrat(7)
print(z)
# cara output 3


# fungsi tambah
def fungsi_tambah(angka1, angka2):
    """fungsi return dengan multi input"""
    return angka1 + angka2


a = fungsi_tambah(10, 10)
print(a)


# fungsi dengan return banyak
def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi


output_tambah, output_kurang, output_kali, output_bagi = operasi_matematika(9, 5)
print(f"Hasil tambah = {output_tambah}")
print(f"Hasil kurang = {output_kurang}")
print(f"Hasil kali = {output_kali}")
print(f"Hasil bagi = {output_bagi}")

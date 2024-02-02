"""Mengenali tentang *Args untuk sebuah data"""
"""args adalah singkatan dari arguments"""


# '''Bagaimana kita mau memasukkan banyak data ke dalam fungsi?'''
# '''kita bisa memakai seperti ini'''
def fungsi(nama, tinggi, berat):
    print(f"nama {nama} tinggi {tinggi} berat {berat}")


fungsi("adrian", 167, 57)


# '''nah, bagaimana agar menjadi simpel?'''
# '''kita pakai data list'''
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"nama {nama} tinggi {tinggi} berat {berat}")


fungsi(["ronaldo", 187, 87])

# '''di program atas ini kan lebih ribet ya ^_^, nah kita dpt menggunakan
# sebuah *args sebuah parameter yang digunakan dalam definisi fungsi untuk
# menangani argumen posisional yang dinamis.'''


"""MENGENAL SEBUAH *args"""


# bisa *args, *data,*nama
# contoh :
# def fungsi(*take):
#     nama = take[0]
#     tinggi = take[1]
#     berat = take[2]
#     print(f"nama {nama} tinggi {tinggi} berat {berat}")


# disini saya pakai *args
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama {nama} tinggi {tinggi} berat {berat}")


fungsi("Pessiun", 120, 90)

"""Pertanyaan? apa untung memakai *args?"""
"""dgn ini, kita dpt menambahkan data tanpa harus ada redudansi"""

"""Contoh : 
dengan seperti ini, ketika di running dan parameternya memakai *, maka kita bisa pakai parameternya yang sama 
dan hasilnya akan baik - baik saja."""
# def tambah(*args):
#     hasil = 0
#     for data in args:
#         hasil += data
#     return hasil


# hasil = tambah(20, 20)
# print(hasil)


# def kali(*args):
#     hasil = 1
#     for data in args:
#         hasil *= data
#     return hasil


# hasil = kali(20, 20)
# print(hasil)

"""Contoh 2: 
dengan seperti ini, ketika di running dan parameternya TIDAK memakai *, maka kita TIDAK bisa pakai 
parameternya yang sama dan outputnya akan ERROR!"""
# def tambah(data):
#     hasil = 0
#     for data in data:
#         hasil += data
#     return hasil


# hasil = tambah(20, 20)
# print(hasil)


# def kali(data):
#     hasil = 1
#     for data in data:
#         hasil *= data
#     return hasil


# hasil = kali(20, 20)
# print(hasil)

"""ITULAH FUNGSI *args atau fungsi adanya * (bintang) di parameternya. agar
tidak perlu mengetik ulang nama parameter / redudansi."""

"""*args tidak harus semestinya memakai *args,bisa kita ubah menjadi
*data,*number,*huruf dll"""


# contoh Studi kasus
def tambah(*data):
    # data tipenya adalah tuple, dan dia bisa di iterasi
    # Iterasi adalah proses berulang kali menjalankan serangkaian instruksi atau
    # pernyataan dalam pemrograman, biasanya menggunakan konsep loop,
    # untuk mencapai tujuan tertentu.
    output = 0
    for i in data:
        output += i
    return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Hasil = {hasil}")
hasil = tambah(10, 15, 5)
print(f"Hasil = {hasil}")


def test(*args):
    print(args)


test(1, 2, 3, 4, 5, "adrian")

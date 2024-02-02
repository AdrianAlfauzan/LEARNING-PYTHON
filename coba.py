def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
    return hasil


hasil = tambah(20, 20)
print(hasil)


def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    return hasil


hasil = kali(20, 20)
print(hasil)

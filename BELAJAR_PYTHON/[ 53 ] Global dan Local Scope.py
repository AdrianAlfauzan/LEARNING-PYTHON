# Global dan local scope

nama_global = "adrian"  # <-- ini adalah variabel global


# akses variabe; global dalam fungsi
def fungsi1():
    print(f"Fungsi menampilkan {nama_global}")


fungsi1()

# akses variabel global dalam loop
for i in range(0, 5):
    print(f"Loop {i} - {nama_global}")

# percabangan

if True:
    print(f"if menampilkan {nama_global}")


# Variabel local scope
def fungsi2():
    nama_local = "adrian - local"  # <-- ini adalah variabel local scope


fungsi2()
# print(nama_local) # tidak bisa dilakukan


# contoh 1 : penggunaan
# JIKA nama = "adrian" di simpan sesuah say_adrian() --> dia tidak akan jalan
# JADI kita harus menyimpannya selalu sebelum say_adrian()
def say_adrian():
    print(f"halo {nama}")


nama = "adrian"
say_adrian()


# contoh 2 : merubah variabel global
angka = 0
name = "leon"


def ubah(nilai_baru, nama_baru):
    global angka  # <-- dia akan bilang bahwa, fungsi ini mendapat akses merubah angka
    angka = nilai_baru
    global name
    name = nama_baru


print(f"Sebelum : {angka} dan {name}")

ubah(10, "prince")
print(f"Sesudah : {angka} dan {name}")


# contoh 3
angka = 0
for i in range(0, 5):
    angka += i
    angka_dummy = 0
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10
print(angka)
print(angka_dummy)

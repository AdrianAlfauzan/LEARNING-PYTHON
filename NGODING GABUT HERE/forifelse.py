jumlah_buku = int(input("Masukkan Jumlah Buku: "))
daftar_buku = []

for i in range(jumlah_buku):
    buku = input(f"Masukkan buku ke-{i}: ")
    daftar_buku.append(buku)

print("Hasil daftar buku:")
for i in daftar_buku:
    print(i)

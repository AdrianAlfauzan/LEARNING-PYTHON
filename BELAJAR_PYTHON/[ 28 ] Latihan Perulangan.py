# Latihan perulangan membuat segitiga

print("AWAL DARI FOR")
sisi = 10
# 1. Menggunakan for
# dummy variabel
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1
print("AKHIR DARI FOR \n")


print("AWAL DARI WHILE")
# 2. Menggunakan while
count = 1
while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break
print("AKHIR DARI WHILE \n")

# 3. hanya ganjil saja
print("AWAL DARI WHILE UNTUK GANJIL")
count = 1
while True:
    if count % 2:
        # Print jika ganjil apabila hasil modulus adalah true (1) dan jika false (0)
        # maka yang akan di jalankan adalah yang else
        print("*" * count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    if count > sisi:
        break
print("AKHIR DARI WHILE UNTUK GANJIL \n")

# Ketika count adalah 2, kondisi dalam blok if count % 2
# tidak akan terpenuhi karena 2 adalah bilangan genap.
# Oleh karena itu, blok if tidak akan dieksekusi.
# Sebaliknya, blok else akan dieksekusi,
# dan pernyataan-pernyataan di dalamnya akan dijalankan.

# Jadi, ketika count adalah 2, maka yang dieksekusi adalah bagian dari blok else.
# Dalam kasus ini, pernyataan print("* genap" * count) akan dijalankan,
# mencetak teks "* genap" dua kali, karena count adalah 2.
# Kemudian, nilai count akan ditambahkan 1 menjadi 3, dan
# loop akan melanjutkan ke iterasi berikutnya.

# 4. Bikin Segitiga
print("WHILE BUAT SEGITIGA AWAL")
count = 1
spasi = int(sisi / 2)
while True:
    if count % 2:
        # Print jika ganjil apabila hasil modulus adalah true (1) dan jika false (0)
        # maka yang akan di jalankan adalah yang else
        print(
            "*" * spasi,
            "*" * count,
        )
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    if count > sisi:
        break
print("WHILE BUAT SEGITIGA AKHIR \n")

# 5. PR bikin KETUPAT
print("WHILE BUAT KETUPAT AWAL")
count = 1
spasi = int(sisi / 2)

sisi_2 = 1
count_2 = 11
spasi_2 = int(sisi_2 / 2)
while True:
    if count % 2:
        # Print jika ganjil apabila hasil modulus adalah true (1) dan jika false (0)
        # maka yang akan di jalankan adalah yang else
        print(
            " " * spasi,
            "*" * count,
        )
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    if count > sisi:
        break


# while True:
#     if count_2 % 2:
#         print(
#             " " * spasi_2,
#             "*" * count_2,
#         )
#         spasi_2 += 1
#         count_2 -= 1
#     else:
#         count_2 -= 1
#         continue
#     if count_2 < sisi_2:
#         break
print("WHILE BUAT KETUPAT AKHIR")

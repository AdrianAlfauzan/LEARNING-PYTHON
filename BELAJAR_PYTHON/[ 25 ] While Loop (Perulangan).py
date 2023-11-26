# while : ketika / saat

# while kondisi (menggunakan boolean) :
#     aksi ini
#     aksi itu

# ---cara 1---
# angka = 10
# while angka > 5:
#     print("Adrian", angka)
#     # angka = 10, lalu 10 lebih dari 5 = TRUE! atau BENAR! jika FALSE / SALAH, dia tidak akan mau jalan.
#     # ketika angka lebih dari 5,maka dia akan menjalankan printnya DAN AKAN TERUS LOOPING.
#     # jika angka kurang dari 5,maka dia tidak akan menjalankan printnya DAN TIDAK AKAN LOOPING.

# ---cara 2---
angka = 0
while angka < 5:
    angka += 1
    print("Adrian", angka)
#   # angka = 0, lalu 0 kurang dari 5 = TRUE! atau BENAR! jika FALSE / SALAH, dia tidak akan mau jalan.
#   # angka += 1 --> 0 + 1 = 1 dan seterusnya...
#   # jadi setiap ketemu (angka += 1) akan ditambah 1
#   # output akan berhenti jika angka 0 lebih besar dari 5

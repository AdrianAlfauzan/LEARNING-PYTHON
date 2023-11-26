# Continue, pass dan break

# Pass --> dia berfungsi sebagai dummy,jadi dia tidak akan di eksekusi.

# -------------------Contoh 1-------------------------
# angka = 0
# while angka < 5:  # ketika angka 0 kurang dari 5, maka
#     angka += 1  # angka akan di tambah 1
#     if angka == 3:  # jika angka sama dengan 3,atau jika angka sudah berada di 3, maka
#         print("Hallo Adrian")  # print "hallo adrian"
#     print(angka)
# -------------------Contoh1-------------------------

# -------------------Contoh2 (Pass)-------------------------
# angka = 0
# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass # Ini tidak akan di eksekusi
#     print(angka)
# -------------------Contoh2 (Pass)-------------------------

# -------------------Contoh3 (Continue)-------------------------
angka = 0
while angka < 5:
    angka += 1
    print(f"Angka sekarang {angka}")  # aksi 1

    if angka == 3:
        print("Hallo Adrian!")
        continue  # dia akan membuat loop meloncat ke step selanjutnya atau dia akan balik lagi ke atas
    # Jadi, apapun yang ada dibawah "continue" atau kalo ketemu "continue" dia akan di skip.
    # intinya, jika ketemu "continue" dia akan DI CUT.
    print("Hallo Programmer!")  # aksi 2
# -------------------Contoh3 (Continue)-------------------------

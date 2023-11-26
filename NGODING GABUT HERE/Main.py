while True:
    maxangkot_input = input("Masukkan jumlah angkot: ")

    if not maxangkot_input.isdigit():
        print("Masukkan harus berupa angka.")
        continue

    maxangkot = int(maxangkot_input)
    
    for angkot in range(1, maxangkot + 1):
        if angkot <= 6:
            print("Angkot No.", angkot, "Berjalan dengan Baik\n")
        elif angkot in range(8, 15):
            print("Angkot No.", angkot, "SUDAH DI JUAL\n")
        else:
            print("Angkot No.", angkot, "Berjalan dengan Buruk\n")

    while True:
        lanjut = str(input("ingin lanjut? (y/n) : "))
        if lanjut == "y":
            break
        elif lanjut == "n":
            print("system berakhir")
            exit()
        else:
            print("Yang anda masukkan salah!")

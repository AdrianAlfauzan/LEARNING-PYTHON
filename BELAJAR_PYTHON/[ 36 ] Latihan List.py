# Membuat database sederhana menggunakan List

# Program List buku
list_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input("judul buku\t : ")
    penulis = input("Nama Penulis\t : ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("No.\t| Judul \t\t| Penulis")
    for index, buku in enumerate(list_buku):
        print(f"{index+1}\t| {buku[0]} \t\t\t| {buku[1]}")

    while True:
        lanjut = str(input("Apakah mau lanjut? (y/n)"))
        if lanjut == "y":
            break
        elif lanjut == "n":
            print("Sytem Out!")
            exit()
        else:
            print("Input tidak valid!")
print("""
[1] ayam goreng \t\t: 25.000
[2] sapi goreng \t\t: 100.000
[3] bebek goreng \t\t: 45.000
[4] babi goreng \t\t: 5.000
""")


total_harga = 0
while True:
    menu = input("Pilih makanan : ")
    porsi = int(input("Mau Berapa Porsi? "))
    if menu == "1":
        menu_ayam = 25000
        hasil = menu_ayam * porsi
        print(f"Harga : {hasil:,}")
    elif menu == "2":
        menu_ayam = 100000
        hasil = menu_ayam * porsi
        print(f"Harga : {hasil:,}")
    elif menu == "3":
        menu_ayam = 45000
        hasil = menu_ayam * porsi
        print(f"Harga : {hasil:,}")
    elif menu == "4":
        menu_ayam = 5000
        hasil = menu_ayam * porsi
        print(f"Harga : {hasil:,}")
    elif not menu.isdigit():
        print("ULANGI!!! PILIH MAKANAN HARUS MENGGUNAKAN NOMOR!!!")
        continue
    else:
        print("Sorry, anda salah input!")
        continue

    subtotal = hasil
    total_harga += subtotal

    tambah_lagi = input("Mau tambah apa lagi? (y/n): ")
    if tambah_lagi.lower() != "y":
        break
    
print("Total Harga : ",total_harga)
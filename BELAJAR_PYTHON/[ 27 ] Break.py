# Break
data_int = int(input("Hitung sampai : "))
angka = 0
while True:
    angka += 1
    print(f"Angka sekarang {angka}")

    if angka == data_int <= 5:
        print("Hallo Adrian!")
        break  # dia akan memberhentikan loopnya.
    elif data_int == angka >= 5:
        print("Kelebihan!")
        break
    print("Hallo Programmer")

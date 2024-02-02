import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    while True:
        # match --> untuk mengecek/memeriksa
        match sistem_operasi:
            # linux, mac, unix --> pakai posix
            # posix itu sama dengan "keys"
            case "posix":
                os.system("clear")
            # windows --> pakai nt
            # nt itu sama dengan "keys"
            case "nt":
                os.system("cls")
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("Masukkan Opsi : ")
        print("\n=========================\n")

        match user_option:
            case "1":
                print(f"1. Read Data")
            case "2":
                print(f"2. Create Data")
            case "3":
                print(f"3. Update Data")
            case "4":
                print(f"4. Delete Data")
        print("\n=========================\n")
        is_done = input("Apakah ingin selesai (y/n) ?")
        if is_done == "y" or is_done == "Y":
            break
    print("Program is Done!")

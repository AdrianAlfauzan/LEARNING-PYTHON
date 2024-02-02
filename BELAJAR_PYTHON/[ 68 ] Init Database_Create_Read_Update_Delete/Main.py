import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name
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

    # check database itu ada atau tidak
    CRUD.init_console()

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
        print(f"5. Ketik 'cls' untuk Berhenti")

        user_option = input("Masukkan Opsi : ")

        match user_option:
            case "1":
                CRUD.read_console()
            case "2":
                CRUD.create_console()
            case "3":
                CRUD.update_console()
            case "4":
                CRUD.delete_console()
            case "cls":
                break
        is_done = input(
            "Ketik 'y/Y' jika ingin Selesai. \nKetik 'n/N' jika ingin kembali ke Menu. \n (y/n) : "
        )
        if is_done == "y" or is_done == "Y":
            break
    print("Program is Done!")

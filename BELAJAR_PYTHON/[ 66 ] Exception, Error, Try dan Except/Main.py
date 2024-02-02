# disini kita akan menghandle runtime Error .
# jadi ini berfungsi untk memberikan notip semisal ada error di tengah jalan.

# [+] Exception --> ini akan terjadi saat program mengalami Error saat Runtime
# Contoh sederhana untuk menangkap Exception
# input_user = int(input("Masukkan angka : "))
# hasil = 0
# try:
#     hasil = 10 / input_user
# except:  # jika terjadi runtime error, maka bilang ...
#     print("Hasil input tidak boleh 0")
# print(f"Hasil = {hasil}")

# [+] Contoh di aplikasi
# while True:
#     angka = int(input("Masukkan angka pembagi : "))
#     try:
#         hasil = 10 / angka
#         print(f"Hasil = {hasil}")
#         is_done = input("Lanjutkan (y/n) ? ")
#         if is_done == "n":
#             break
#     except:
#         print("Pembagi nya 0, silahkan masukkan kembali program")
# print("PROGRAM IS DONE!")

# [+] Contoh dalam open file
try:
    with open(
        "D:\\BELAJAR FT MY CODING\\BELAJAR PYTHON\\BELAJAR_PYTHON\\[ 66 ] Exception, Error, Try dan Except\\data.txt",
        "r",
    ) as file:
        print(file.read)
except:
    print("File data.txt Tidak di temukan, membuat file baru")
    with open(
        "D:\\BELAJAR FT MY CODING\\BELAJAR PYTHON\\BELAJAR_PYTHON\\[ 66 ] Exception, Error, Try dan Except\\data.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write("File baru")
else:
    print("File telah terbuat.")

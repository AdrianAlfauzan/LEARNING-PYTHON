"""**kwargs"""


# contoh awal
def fungsi(nama, tinggi, berat):
    """fungsi biasa"""
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("adrian", 182, 72)


# outputnya ini seperti dictionary
# ini bisa juga **data,**nama,**output --> BEBAS
def fungsi(**output):
    """fungsi kwargs"""
    nama = output["nama"]
    tinggi = output["tinggi"]
    berat = output["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    # [nama] --> kita ambil key nya
    # print(output["nama"])


fungsi(nama="adrian", tinggi=182, berat=72)

# kwargs ini bisa membuat opsi juga
# contoh studi kasus


def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operasi")
    return output


hasil = math(1, 2, 3, 4, option="tambah")
print(f"hasil tambah = {hasil}")
hasil = math(1, 2, 3, 4, 5, 6, 7, option="kali")
print(f"hasil tambah = {hasil}")

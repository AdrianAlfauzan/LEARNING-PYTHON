# Nested list atau List Bersarang
# Membuat list di dalam List

data_0 = [1, 2]
data_1 = [3, 4]
data_list_biasa = [1, 2, 3, 4]
print(f"List Biasa = {data_list_biasa}")

list_2d = [data_0, data_1]
print(f"List 2D = {list_2d}")

# Contoh penggunaan
peserta_0 = ["adrian", 20, "Laki-Laki"]
peserta_1 = ["Otong", 10, "Laki-Laki"]
peserta_2 = ["Shifa", 30, "Wanita"]
list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"List Peserta : {list_peserta}")

# Cara ngeprint dia supaya bisa di tampilkan jadi rapih
for peserta in list_peserta:
    print(f"Nama : {peserta[0]}")
    print(f"umur : {peserta[1]}")
    print(f"Kelamin : {peserta[2]}\n")


# problemnya : bagaimana caranya mengcopy ini semua ?
# dengan reference
list_peserta_copy = list_peserta.copy()
print(f"List Peserta Copy : {list_peserta_copy}")
peserta_0[0] = "Ronaldo"
print(f"List Peserta Copy = {list_peserta_copy}")
print(f"List Peserta Asli = {list_peserta}")
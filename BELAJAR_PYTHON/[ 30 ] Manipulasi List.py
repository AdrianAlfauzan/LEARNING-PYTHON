# Operasi pada list

# index   0(-3)     1(-2)     2(-1)
data = ["Adrian", "kakang", "ahmad"]

# cara mengambil dara dari list di atas
data_0 = data[0]
print(f"Data pertama (index-0) {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir (index-(-1)) {data_terakhir}")

data_kakang = data[1]
print(f"Data terakhir (index-1) {data_kakang}")

# mengambil jumlah data dalam list
panjang_data = len(data)
print(f"Panjang Data adalah {panjang_data}")

# Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"Data sebelum ditambah {data}")

data.insert(1, "Musa")
print(f"Data Sesudah ditambah {data}")

# Menambah di akhir list
data.append("Alfauzan")
print(f"Data ditambah di akhir {data}")

# Menambahkan list dengan list
data_baru = ["ronaldo", "messi", "neymar"]
data.extend(data_baru)
print(f"Data Gabungan {data}")


# Merubah data
# Kita ubah data 2 menjadi GOAT
data[2] = "GOAT"
print(f"Data Kakang telah diubah! {data}")

# Meremove data
data.remove("messi")
print(f"Data messi telah Di hapus! {data}")

# Meremove data paling akhir
data.pop()
print(f"Data paling akhir telah di hapus! {data}")

# melihat data yang dihapus
data_remove = "ronaldo"
data.remove(data_remove)
print(f"Data yang di hapus : {data_remove}")
print(data)

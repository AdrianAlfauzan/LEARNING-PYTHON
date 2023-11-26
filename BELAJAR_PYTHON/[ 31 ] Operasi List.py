data_angka = [1, 2, 5, 8, 5, 6, 8, 2, 9, 0, 4, 3, 6]
print(f"data angka : {data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
print(f"Jumlah data 4 ada --> {jumlah_data_4}")

jumlah_data_6 = data_angka.count(6)
print(f"Jumlah data 6 ada --> {jumlah_data_6}")

# Ambil posisi data
data = ["Ronaldo", "Messi", "Neymar", "Benzema"]
print(f"Data : {data}")

index_ronaldo = data.index("Ronaldo")
print(f"Index dari ronaldo : {index_ronaldo}")

index_benzema = data.index("Benzema")
print(f"Index dari benzema : {index_benzema}")

# Mengurutkan List
print("Data angka sebelum sort :", data_angka)
data_angka.sort()
print(f"data sort dari angka : {data_angka}")

print("Data String sebelum Sort :", data)
data.sort()
print(f"data sort dari string : {data}")

# Membalik list
data_angka.reverse()
print(f"data reverse dari angka : {data_angka}")
data.reverse()
print(f"data reverse dari String : {data}")

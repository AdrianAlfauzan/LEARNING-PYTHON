# List
data_list = [12, 45, 22]  # menggunakan kurung siku
print(data_list)
# bisa di ambil datanya
print(data_list[1])


# Tuples --> ini penting untuk machine learning,django dll
data_tuples = (1, 2, 3, 4, 5, 6)
print(data_tuples)
# bisa di ambil datanya
print(data_tuples[1])

# --> LARANGAN : 
# tidak dapat rubah isinya yang artinya datanya FIX!
# data_tuples[2] = "adrian"
# tidak dapat di tambah isinya juga
# data_tuples.append(100)

# Sets --> sebuah collection yang tidak memiliki index
# data ini adalah himpunan yang dimana tidak ada urutannya
data_sets = {6, 8, 3, 1, 0, 4, 5, 2, 9}
print(data_sets)

# --> LARANGAN : 
# Ga bisa di ambil datanya
# Ga bisa indexing saja
# print(data_sets[0])

# sets bisa kita append,hitung count dll

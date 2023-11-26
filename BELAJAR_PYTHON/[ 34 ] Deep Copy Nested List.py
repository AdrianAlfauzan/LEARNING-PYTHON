data_0 = [1, 2]
data_1 = [3, 4]

data_2d = [data_0, data_1,10]
data_2d_copy = data_2d.copy()
print(f"Data : {data_2d}")
print(f"Data Copy : {data_2d_copy}")

# Mengambil data di dalam Nested list
# 0 --> step awal
# 1 --> step akhir
data = data_2d[0][1]
print(f"Mengambil Data : {data}")

# Address semuanya
print(f"Address data_2d : {hex(id(data_2d))}")
print(f"Address data_2d Copy : {hex(id(data_2d_copy))}")

print("Address dari member ke- 1 ")
print(f"Address data_2d : {hex(id(data_2d[0]))}")
print(f"Address data_2d Copy : {hex(id(data_2d_copy[0]))}")

data = data_2d[0][1] = 8
data_2d[2] = 9
print(f"Data 2d : {data_2d}")
print(f"Data Copy : {data_2d_copy}")


print("\n----------Menggunakan DeepCopy-----------")
# Kita gunakan deepcopy
from copy import deepcopy
data_2d = [data_0, data_1,10]
data_2d_deepcopy = deepcopy(data_2d)
print(f"Address data_2d Asli : {hex(id(data_2d))}")
print(f"Address data_2d DeepCopy : {hex(id(data_2d_deepcopy))}")

print("Address dari member ke- 1 ")
print(f"Address data_2d : {hex(id(data_2d[0]))}")
print(f"Address data_2d DeepCopy : {hex(id(data_2d_deepcopy[0]))}")

data = data_2d[0][1] = 100
print(f"Data Asli : {data_2d} {hex(id(data_2d))}")
print(f"Data Copy : {data_2d_copy} {hex(id(data_2d_copy))}")
print(f"Data DeepCopy : {data_2d_deepcopy} {hex(id(data_2d_deepcopy))}")
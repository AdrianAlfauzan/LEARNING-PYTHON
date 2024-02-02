# Tipe data : Angka satuan (Integer)


# Menggunakan metode format
# data_integer = 1
# print("Data Format : {}".format(data_integer))
# print("Bertipe Format : {}".format(type(data_integer)))


data_integer = 1
print("Data :", data_integer)
print("Bertipe : ", type(data_integer))

# Tipe data : Angka dengan koma (float)
data_float = 1.5
print("Data :", data_float)
print("Bertipe : ", type(data_float))

# Tipe data : Kumpulan Karakter (String)
data_string = "Adrian"
print("Data :", data_string)
print("Bertipe : ", type(data_string))

# Tipe data : Biner True/False (Boolean)
data_boolean = True
print("Data :", data_boolean)
print("Bertipe : ", type(data_boolean))

# Tipe data khusus
# Bilangan kompleks
data_complex = complex(5, 6)
print("Data :", data_complex)
print("Bertipe : ", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data :", data_c_double)
print("Bertipe : ", type(data_c_double))

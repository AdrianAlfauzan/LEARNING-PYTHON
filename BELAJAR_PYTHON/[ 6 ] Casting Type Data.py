# Casting adalah merubah dari 1 tipe ke tipe lain

# INTEGER
print("-------------INTEGER--------------")
data_integer = 1
print("Data :", data_integer)
print("Bertipe : ", type(data_integer))

data_float = float(data_integer)
print("Data :", data_float)
print("Bertipe : ", type(data_float))

data_string = str(data_integer)
print("Data :", data_string)
print("Bertipe : ", type(data_string))

data_boolean = bool(data_integer)  # Akan false jika nilai integer adalah 0
print("Data :", data_boolean)
print("Bertipe : ", type(data_boolean))

print("-------------FLOAT--------------")

# FLOAT
data_float = 7.5
print("Data :", data_float)
print("Bertipe : ", type(data_float))

data_integer = int(data_float)
print("Data :", data_integer)
print("Bertipe : ", type(data_integer))

data_string = str(data_float)
print("Data :", data_string)
print("Bertipe : ", type(data_string))

data_boolean = bool(data_float)  # Akan false jika nilai integer adalah 0
print("Data :", data_boolean)
print("Bertipe : ", type(data_boolean))

print("-------------BOOLEAN--------------")
# BOOLEAN
data_boolean = True  # Akan false jika nilai integer adalah 0
print("Data :", data_boolean)
print("Bertipe : ", type(data_boolean))

data_integer = int(data_boolean)
print("Data :", data_integer)
print("Bertipe : ", type(data_integer))

data_string = str(data_boolean)
print("Data :", data_string)
print("Bertipe : ", type(data_string))

data_float = float(data_boolean)
print("Data :", data_float)
print("Bertipe : ", type(data_float))

print("-------------STRING--------------")

# FLOAT
data_string = "10"
print("Data :", data_string)
print("Bertipe : ", type(data_string))

data_integer = int(data_string)  # Harus Angka
print("Data :", data_integer)
print("Bertipe : ", type(data_integer))

data_float = float(data_string)  # Harus Angka
print("Data :", data_float)
print("Bertipe : ", type(data_float))

# Akan false jika stringnya kosong
# akan tetapi int dan float perlu di command terlebih dahulu
data_boolean = bool(data_string)
print("Data :", data_boolean)
print("Bertipe : ", type(data_boolean))

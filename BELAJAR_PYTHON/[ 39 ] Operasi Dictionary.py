# Operator Dictionary


data_dict = {
    "an" : "adrian",
    "rnl" : "ronaldo",
    "ps" : "pessi"
}

# Panjang Dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary : {LENDICT}")

# Mengecek key ada atau tidak
KEY1 = "an"
CHECKKEY1 = KEY1 in data_dict
print(f"Apakah data '{KEY1}' ada di data_dict : {CHECKKEY1}")

KEY2 = "lmn"
CHECKKEY2 = KEY2 in data_dict
print(f"Apakah data '{KEY2}' ada di data_dict : {CHECKKEY2}")
# Mengakses Value (Read) dgn Get
print(data_dict["an"])
print(data_dict.get("an"))
print(data_dict.get("kaka","Key tidak ditemukan.")) # cek key dengan message.

# Mengupdate Data
data_dict["an"] = "adrian is programmer Software Engineering"
print(data_dict)
data_dict["rnl"] = "Ronaldo is GOAT"
print(data_dict)


# Memakai updaate, sistemnya seperti ini :
# jika data sudah ada, maka dia akan update data yang sudah ada
# jika data nya belum ada, dia akan menambah datanya
data_dict.update({"Neymar":"Neymar jr"})
print(data_dict)

# Mendelete data pada dictionary
del data_dict["ps"]
print(data_dict)
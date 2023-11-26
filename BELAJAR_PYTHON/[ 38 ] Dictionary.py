# List --> ini contoh dari array, mengakses dengan

# menggunakan index
data_list = ["adrian", "musa", "alfauzan"]
print(data_list[1])

# Dictionary (dict) --> kita sebut dengan Associative array
# Kalo di list kita mengakses menggunakan indexnya
# kalo di associative array kita mengakses menggunakan identifier
# identifier --> key

# Contoh syntaxnya :
# data_dict = {
#     "key1":"value1",
#     "key2":"value2"
# }
# print(data_dict)

data_dict = {
    "ind": "indonesia",
    "russ": "russia",
    "jp": "japan",
    "nmbr": 100,
    "list": data_list,
}
print(data_dict["ind"])
print(data_dict["nmbr"])
print(data_dict["list"])

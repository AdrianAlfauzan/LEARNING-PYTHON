# LIST

# kumpulan data numbers

data_angka = [1, 2, 3]
print(data_angka)

# kumpulan data string
data_string = ["adrian", "musa", "nadya"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1, "pizza", 2, "burger", "mcdonald", False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0, 10, 2)  # dia bukan data list,tapi
# 0 = start
# 10 = akhir
# 2 = increment/step nya
print(data_range)
data_list = list(data_range)  # kita bisa pakai "list" agar menjadi list.
print(data_list)

# membuat list dengan for loop,list comprehension
data_list_for = [i for i in range(0, 10)]
# penjelasan :
# didalam "data_list_for" saya ingin memasukkan "i"
# dimana "i" untuk "i" di dalam range 0 - 10
print(data_list_for)

data_list_for_pangkat = [i**2 for i in range(0, 10)]
# penjelasan :
# i**2 artinya di pangkatkan 2
# didalam "data_list_for" saya ingin memasukkan "i"
# dimana "i" untuk "i" di dalam range 0 - 10
print(data_list_for_pangkat)

# membuat list pake for pake if
data_list_for_if = [i for i in range(0, 10) if i != 5]
# penjelasan :
# didalam "data_list_for_if" saya ingin memasukkan "i"
# dimana "i" untuk "i" di dalam range 0 - 10
# jika i tidak sama dengan (!=) 5
# maka nomor 5 akan hilang di data listnya!
print(data_list_for_if)

# ini untuk genap
data_list_for_if = [i for i in range(0, 10) if i % 2 == 0]
# penjelasan :
# didalam "data_list_for_if" saya ingin memasukkan "i"
# dimana "i" untuk "i" di dalam range 0 - 10
# jika i di modulus (%) 2, sama dengan (==) 0
# maka outputnya akan genap

# kenapa genap? karena...
# if i%2 == 0
# jika i di modulus 2 == 0
# i start --> 0 sampai 10
# jika i (1,2,3,4,5,6,7,8,9,10) yang di modulus 2 hasilnya 0,maka akan di outputkan.
# contoh :
# i ke 0 di modulus 2 = 0 , [TRUE/BENAR] (kita minta hasilnya yang 0,karena == 0), maka di outputkan 0
# i ke 1 di modulus 2 = 1 , [FALSE/SALAH] (kita minta hasilnya yang 0,karena == 0)
# i ke 2 di modulus 2 = 0 , [TRUE/BENAR] (kita minta hasilnya yang 0,karena == 0), maka di outputkan 2

print(data_list_for_if)

# ini untuk ganjil
data_list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(data_list_for_if)

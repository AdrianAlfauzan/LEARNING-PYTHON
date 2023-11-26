# Looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka:
    # Angka --> variabel
    # si angka yg ada di kumpulan_angka. jadi setiap satu putaran
    # dia akan mengambil komponen-komponennya
    print(f"angka = {angka}")

peserta = ["Neymar", "ronaldo", "pessi", "mbappe"]
for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10, 5, 4, 2, 6]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"Angka = {kumpulan_angka}")

# while
print("\nWhile loop")
kumpulan_angka = [10, 5, 4, 2, 6]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka}")
    i += 1

# List comprehension
print("\nList Comprehension")
data = ["Ronaldo",1,2,3,"pessi"]
[print(f"data = {i}") for i in data]

# Enumerate --> dia akan mengambil indexnya dan datanya
print("\nEnumerate")
data_list = ["Ronaldo",1,2,3,"pessi"]

# Number --> index
for number, data in enumerate(data_list):
    print(f"number = {number} , data = {data}")

# Data kuadrat
print("\nData kuadrat")
angka = [10,4,6,20,3]
angka_kuadrat = [i**2 for i in angka]
print(f"Angka kuadrat = {angka_kuadrat}")
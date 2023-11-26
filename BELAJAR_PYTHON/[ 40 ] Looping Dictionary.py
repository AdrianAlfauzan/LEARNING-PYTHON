# Looping dictionary

teman_teman = {
    "rnl": "ronaldo",
    "pes": "pessi",
    "an": "adrian",
    "mar": "neymar",
    "han": "arhan",
}

# Looping first try --> yang keluar hanya KEY nya saja
print("\n mengambil KEY :")
for teman in teman_teman:
    print(teman)

# Operator untuk mengambil item / iterables (iterasi/iteration)
print("\n Mengambil KEY dgn Operasi Iterables :")
keys = teman_teman.keys()
print(keys)

print("\n mengambil KEY :")
for kunci in teman_teman.keys():
    print(kunci)

print("\n mengambil isi DATA KEY :")
for kunci in teman_teman.keys():
    print(teman_teman.get(kunci))

# Mengambil Value
print("\n mengambil Value dgn Operasi Iterables:")
values = teman_teman.values()
print(values)

print("\n mengambil isi DATA VALUE :")
for value in teman_teman.values():
    print(value)

# Mengambil items
print("\n mengambil SEMUA ITEMS dgn Iterables:")
items = teman_teman.items()
print(items)

print("\n mengambil ITEMS :")
for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}\t|\tValue = {value}")

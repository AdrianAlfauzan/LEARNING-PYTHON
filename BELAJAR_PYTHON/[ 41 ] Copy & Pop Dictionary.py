# Copy Dictionary
print("\n COPY DICTIONARY :")
teman_teman = {
    "rnl": "ronaldo",
    "pes": "pessi",
    "an": "adrian",
    "mar": "neymar",
    "han": "arhan",
}
print("\n SEBELUM DI COPY :")
print(f"Teman - Teman : {teman_teman} \n")

print("\n SESUDAH DI COPY :")
friends = teman_teman.copy()
print(f"Friends : {friends} \n")

print("\n PERBEDAAN SETELAH DI COPY:")
teman_teman["an"] = "ADRIAN"
print(f"Teman - Teman : {teman_teman} \n")
print(f"Friends : {friends} \n")


# Pop Dictionary --> kita ambil berdasarkan key
print("\n POP DICTIONARY :")
data_Ronaldo = friends.pop("rnl")
print(f"DATA RONALDO : {data_Ronaldo}")

print("\n HASIL :")
print(f"Teman - Teman : {teman_teman} \n")
print(f"Friends : {friends} \n")

# Popitem Dicionary --> kita ambil yang terakhir saja
print("\n POP ITEM DICTIONARY :")
data_terakhir = friends.popitem()

print("\n HASIL :")
print(f"DATA TERAKHIR : {data_terakhir}")
print(f"Friends : {friends} \n")

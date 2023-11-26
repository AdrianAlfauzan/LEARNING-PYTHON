# Tehnik Menduplikat List
data_a = ["Ronaldo", "Messi", "Neymar", "Benzema"]
print(f"Data a = {data_a}")

data_b = data_a  # Pass by reference
print(f"Data b = {data_b}")


# Kita akan merubah Member Data A
# Ini akan merubah kedua list
data_a[1] = "Kaka"
data_b.sort()
print(f"Data a = {data_a}")
print(f"Data b = {data_b}")

# Address dari kedua List data_a dan data_b
print(f"Address data a = {hex(id(data_a))}")
print(f"Address data b = {hex(id(data_b))}")

print("\nMembuat list data_c dengan data_a.copy()")
# Menduplikat List dgn Copy
data_c = data_a.copy()  # Full duplikat / data baru
print(f"Address data a = {hex(id(data_a))}")
print(f"Address data b = {hex(id(data_b))}")
print(f"Address data c = {hex(id(data_c))}")

print(f"Data a = {data_a}")
print(f"Data b = {data_b}")
print(f"Data c = {data_c}")

print("\nMengubah Data dgn .copy()")

data_c[2] = "Talisca"
print(f"Data a = {data_a}")
print(f"Data b = {data_b}")
print(f"Data c = {data_c}")

data_c[0] = "Kepa"
print(f"Data a = {data_a}")
print(f"Data b = {data_b}")
print(f"Data c = {data_c}")

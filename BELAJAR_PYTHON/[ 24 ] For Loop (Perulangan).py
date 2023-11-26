# Perulangan (Loop)

# for kondisi:
#     aksi

print(5 * "=", "ini dengan list", "=" * 5)
angka2_list = [0, 1, 2, 3, 4]  # ini adalah list
print(angka2_list)
for i in angka2_list:  # penjelasan :  Untuk i didalam angka2_list
    print(f"i sekarang -> {i}")

print("\n", 5 * "=", "ini dengan range", "=" * 5)
# ini dengan range
angka2_range = range(5)
for i in angka2_range:
    print(f"i sekarang -> {i}")

print("\n")

angka2_range = range(1, 5)
# ini dengan pembatas. jadi mulai dari 1 dan di akhiri dengan 5 tapi 5 nya tidak di ambil.
for i in angka2_range:
    print(f"i sekarang -> {i}")

print("\n")

for i in range(1, 10):
    print("Gua ke ", i)

print("\n", 5 * "=", "ini dengan string", "=" * 5)
# Menggunakan String
data_str = "saya adalah gamers"
for huruf in data_str:
    print(huruf)  # outputnya akan menjadi perhuruf.

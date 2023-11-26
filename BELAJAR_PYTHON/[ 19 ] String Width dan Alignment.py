# Width and Alignment

# Data

data_nama = "Adrian Musa"
data_umur = 20
data_tinggi = 167.8
data_hobi = "Hacking"

# string
print(5 * "=", "DATA STRING", "=" * 5)
data_string = (
    f"Nama {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, hobi = {data_hobi}"
)
print(data_string)

# string multiline (dengan menggunakan enter, newline, atau \n)
print("\n", 5 * "=", "DATA STRING", "=" * 5)
data_string = f"Nama {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nhobi = {data_hobi}"
print(data_string)

# String multiline (kutip triplets)
print("\n", 5 * "=", "DATA STRING", "=" * 5)
data_nama = "Adrian"
data_string = f"""nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
hobi   = {data_hobi}
"""
print(data_string)

# Mengatur lebar
print("\n", 5 * "=", "DATA STRING", "=" * 5)
data_nama = "Adrian"
data_string = f"""nama   = {data_nama:>10}
umur   = {data_umur}
tinggi = {data_tinggi}
hobi   = {data_hobi}
"""
# tanda :>10 itu untuk menggeser lebarnya ke kanan agar lebih rapih
print(data_string)

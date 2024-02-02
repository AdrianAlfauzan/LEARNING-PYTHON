# __init__ adalah satu file yang ada di dalam folder package, ini itu harus ada
# walaupun terkadang tidak ada

# tidak akan berfungsi untuk penggunaan __all__
import sains  # import dari folder sains

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil Tambah = {hasil_tambah}")

hasil_kali = sains.matematika.kali(10, 10)
print(f"Hasil Kali = {hasil_kali}")

hasil_pangkat = sains.matematika.pangkat(3)
print(f"Hasil Pangkat = {hasil_pangkat(5)}")

hasil_fisika = sains.fisika.gaya(10, 9)
print(f"Hasil Fisika = {hasil_fisika}")

# untuk __all__ saja! akan tetapi tidak di sarankan untuk digunakan
# ini hanya untuk pengetahuan jika menemukan hal seperti ini!
# from sains import *

# hasil_tambah = matematika.basic.tambah(1, 2, 3, 4, 5)
# print(f"Hasil Tambah = {hasil_tambah}")

# hasil_kali = matematika.basic.kali(10, 10)
# print(f"Hasil Kali = {hasil_kali}")

# hasil_fisika = fisika.gaya(10, 9)
# print(f"Hasil Fisika = {hasil_fisika}")

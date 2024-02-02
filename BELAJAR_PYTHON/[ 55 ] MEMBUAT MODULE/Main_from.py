# Module matematika dengan from

from matematika import tambah, kali  # ini cara import dari folder apa dan isi nya apa
from matematika import *  # artinya mengambil semua yang ada di folder/module matematika


hasil_tambah = tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = kali(1, 2, 3, 4, 5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"Hasil Pangkat3 = {pangkat_3(3)}")

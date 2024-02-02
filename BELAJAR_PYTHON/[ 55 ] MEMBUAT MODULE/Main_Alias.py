# Module matematika dengan alias

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as pkt

# dari folder matematika, kita import tambah sebagai add
# as --> bebas mau kasih nama apa saja

import matematika as math  # <--- bisa dilakukan juga

hasil_tambah = add(1, 2, 3, 4, 5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = k(1, 2, 3, 4, 5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = pkt(3)
print(f"Hasil Pangkat3 = {pangkat_3(3)}")

# bisa tambah,kali dan pangkat
hasil_kali = math.kali(1, 2, 3, 4, 5)
print(f"Hasil kali = {hasil_kali}")

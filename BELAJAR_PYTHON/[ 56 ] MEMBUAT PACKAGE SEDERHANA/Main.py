# cara bacanya :
# kita import package, yang didalamnya ada module matematika
import sains.matematika

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah = {hasil_tambah}")

# import sains.fisika

from sains import fisika

hasil = fisika.gaya(25, 25)
print(f"Hasil = {hasil}")

# from sains yang ada file fisika, import yang di dalamnya ada gaya
from sains.fisika import gaya  # untuk satu panggilan

gaya = sains.fisika.gaya(90, 10)
print(f"gaya adalah = {gaya}")

# jika ada 2 panggilan, pakai as agar dapat memanggil secara berulang
from sains.fisika import gaya as gaya2

gaya = gaya2(90, 10)
print(f"gaya adalah = {gaya}")

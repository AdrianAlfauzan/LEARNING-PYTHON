# Date and Time (Latihan)

import datetime as dt

print("\n", 5 * "=", "Latihan", "=" * 5)

print("Silahkan masukan tanggal, bulan dan tahun : ")
tahun = int(input("tahun \t\t:"))
bulan = int(input("bulan \t\t:"))
tanggal = int(input("Tanggal \t:"))
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda : {tanggal_lahir}")
print(f"Anda Lahir Pada Hari : {tanggal_lahir:%A}")

# %A: Nama hari lengkap (misalnya: Senin, Selasa, Rabu).
# %a: Nama hari singkat (misalnya: Sen, Sel, Rab).
# %d: Hari dalam format dua digit (01-31).
# %B: Nama bulan lengkap (misalnya: Januari, Februari, Maret).
# %b atau %h: Nama bulan singkat (misalnya: Jan, Feb, Mar).
# %m: Bulan dalam format dua digit (01-12).
# %Y: Tahun dalam format empat digit.
# %y: Tahun dalam format dua digit (misalnya: 21 untuk 2021).
# %H: Jam dalam format 24 jam (00-23).
# %I: Jam dalam format 12 jam (01-12).
# %M: Menit dalam format dua digit (00-59).
# %S: Detik dalam format dua digit (00-59).
# %p: AM atau PM, hanya berlaku saat menggunakan format jam 12 jam.

print("\n", 5 * "=", "Latihan", "=" * 5)
hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
print("Umur Hari", umur_hari)
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
sisa_hari = umur_hari.days % 365
print(f"Umur anda adalah : {umur_tahun} Tahun, {umur_bulan} Bulan, {sisa_hari} Hari")

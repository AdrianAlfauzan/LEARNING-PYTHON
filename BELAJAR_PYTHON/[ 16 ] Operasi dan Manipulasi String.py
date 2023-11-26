# 1. menyambung string (concatenate)

nama_pertama = "AdriaN"
nama_tengah = "M"
nama_akhir = "AlfauZan"
nama_lengkap = nama_pertama + "'" + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang Nama ", nama_lengkap, "adalah", panjang)

# 3. operator untuk string
# apakah ada komponen char atau string di stringnya

M = "M"
status = M in nama_lengkap
print("String", M, "di", nama_lengkap, "adalah", str(status))

X = "X"
status = X not in nama_lengkap
print("String", X, "di", nama_lengkap, "adalah", str(status))

# mengulang string
print("HAHA" * 10)

# mencari index atau indexing
print("index ke-0 : dari nama ", nama_lengkap, "adalah", nama_lengkap[0])
print("index ke-1 : dari nama ", nama_lengkap, "adalah", nama_lengkap[1])
print("index ke-1 : dari nama ", nama_lengkap, "adalah", nama_lengkap[7])

# memakai (minus),itu artinya menghitung mulai dari belakang
print("index ke - (-1) : dari nama ", nama_lengkap, "adalah", nama_lengkap[-1])
print("index ke - (-2) : dari nama ", nama_lengkap, "adalah", nama_lengkap[-2])

# dimulai dari index 0 - 3, akan tetapi index yang terakhir tidak di cantumkan
print("index ke - [0 - 3] : dari nama ", nama_lengkap, "adalah", nama_lengkap[0:3])
print("index ke - [0 - 3] : dari nama ", nama_lengkap, "adalah", nama_lengkap[0:3])

# memakai jeda
# cara bacanya :
# 0 artinya index yang dimulai
# 10 artinya hingga index ke 10
# 2 artinya diloncatin 2 atau diimplemen 2
print(
    "index ke - [0,2,4,6,8,10] : dari nama ",
    nama_lengkap,
    "adalah",
    nama_lengkap[0:10:2],
)

# item paling kecil atau urutan abjad paling awal (a,b,c,d) paling awal = a
print("paling kecil : ", min(nama_lengkap))
# item paling besar atau urutan abjad paling akhir (v,w,x,y,z) paling akhir = z
print("paling besar : ", max(nama_lengkap))

# Mengetahui nilai dari huruf,simbol dll dengan ascii code!
ascii_code = ord("'")
print("ASCII code untuk Kutip (') adalah", str(ascii_code))
ascii_code2 = ord("a")
print("ASCII code untuk huruf (a) adalah", str(ascii_code2))
ascii_code3 = ord("u")
print("ASCII code untuk huruf (u) adalah", str(ascii_code3))

data = 117
print("Char untuk ASCII 117 adalah", chr(data))


# 4. Operator dalam bentuk method atau menghitung jumlah huruf yang sama!
data = "ronaldo cristiano"
jumlah = data.count("o")
print("Jumlah huruf O pada", data, "=", str(jumlah))

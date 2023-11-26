# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is dan is not

a = 4
b = 2

# lebih besar dari ">"
print("-----Lebih Besar Dari (>)-----")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

# Kurang dari "<"
print("-----Lebih Besar Dari (<)-----")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

# Lebih dari sama dengan ">="
print("-----Lebih Dari Sama Dengan (>=)-----")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

# Kurang dari sama dengan "<="
print("-----Kurang Dari Sama Dengan (<=)-----")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

# sama dengan "==" yang artinya membandingkan antara 2 buah nilai
print("-----Sama Dengan (==)-----")
hasil = a == 4
print(a, "==", 4, hasil)
hasil = b == 4
print(b, "==", 4, hasil)

# Tidak sama dengan "!=" yang artinya membandingkan antara 2 buah nilai
print("-----Sama Dengan (!=)-----")
hasil = a != 4
print(a, "!=", 4, hasil)
hasil = b != 4
print(b, "!=", 4, hasil)

# "Is" Sebagai komparasi object identity
print("-----Object Identity (is)-----")
x = 5  # ini adalah assignment membuat object
y = 5
print("Nilai x =", x, "id =", hex(id(x)))
print("Nilai y =", y, "id =", hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

# "Is Not" Sebagai komparasi object identity
print("-----Object Identity (is not)-----")
x = 5  # ini adalah assignment membuat object
y = 10
print("Nilai x =", x, "id =", hex(id(x)))
print("Nilai y =", y, "id =", hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

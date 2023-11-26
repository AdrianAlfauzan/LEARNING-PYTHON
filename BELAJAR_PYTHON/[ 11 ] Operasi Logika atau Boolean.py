# Operasi logika atau boolean

# not, or , and , xor - (operasi yang dilakukan untuk boolean)

# NOT
print("=====NOT=====")
a = False
c = not a
print("data a = ", a)
print("jika di NOT akan menjadi :")
print("data c = ", c)

# OR (Disjungsi -> jika salah satunya TRUE maka dia akan TRUE)
print("=====OR=====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (Konjungsi -> jika salah satunya FALSE maka dia akan FALSE)
print("=====AND=====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

# XOR (akan TRUE jika salah satunya TRUE,sisanya FALSE)
print("=====XOR=====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

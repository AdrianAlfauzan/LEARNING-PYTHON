# Latihan percabangan

# Kalkulator sederhana

print(20 * "=")
print("Kalkulator Sederhana")
print(20 * "=")

angka_1 = float(input("Masukkan angka pertama : "))
operator = input("Operator (x,/,+,-,//,%) : ")
angka_2 = float(input("Masukkan angka kedua : "))

if operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil:.0f}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil:.0f}")
elif operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil:.0f}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil:.0f}")
elif operator == "//":
    hasil = angka_1 // angka_2
    print(f"Hasilnya adalah {hasil:.0f}")
elif operator == "%":
    hasil = angka_1 % angka_2
    print(f"Hasilnya adalah {hasil:.0f}")
else:
    print("Terdapat kesalahan pada Operator")

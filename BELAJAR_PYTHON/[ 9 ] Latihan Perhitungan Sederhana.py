# lATIHAN KONVERSI SATUAN TEMPERATUR

# PROGRAM KONVERSI CELCIUS KE SATUAN LAIN

print("/n PROGRAM KONVERSI TEMPERATUR")

# CELCIUS
celcius = float(input("Masukan suhu dalam celcius : "))
print("Suhu adalah", celcius, "celcius")

# REAMUR
reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah", reamur, "reamur")


# FAHRENHEIT
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")


# KELVIN
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "kelvin")

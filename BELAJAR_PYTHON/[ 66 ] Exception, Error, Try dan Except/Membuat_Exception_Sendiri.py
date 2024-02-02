# Contoh membuat exception sendiri

# from numbers import Number


# def tambah(a, b):
#     if not isinstance(a, Number) or not isinstance(b, Number):
#         raise TypeError("Input pertama dan kedua harus angka")
#     return a + b


# print(tambah(5, "v"))


# Menangkap berdasarkan type exceptionnya
from decimal import DivisionByZero

angka = 0

try:
    hasil = 10 / angka
except Exception as error_message:
    print(error_message)

# atau

angka = 0

try:
    hasil = 10 / angka
except ZeroDivisionError as error_message:
    print(error_message)

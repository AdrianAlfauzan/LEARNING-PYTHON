def fibonacci(n):
    fibonacci_series = []
    if n == 0:
        return fibonacci_series
    elif n == 1:
        fibonacci_series.append(0)
        return fibonacci_series
    elif n == 2:
        fibonacci_series.extend([0, 1])
        return fibonacci_series
    else:
        fibonacci_series.extend([0, 1])

        for i in range(2, n):
            fibonacci_series.append(fibonacci_series[i - 1] + fibonacci_series[i - 2])

        return fibonacci_series

# Menerima input jumlah bilangan Fibonacci dari pengguna
jumlah_bilangan = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))

# Memanggil fungsi fibonacci dan menyimpan hasilnya
deret_fibonacci = fibonacci(jumlah_bilangan)

# Menampilkan deret bilangan Fibonacci
print(f"Deret Fibonacci dengan {jumlah_bilangan} bilangan:")
for bilangan in deret_fibonacci:
    print(bilangan)
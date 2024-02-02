import numpy as np

"""kegunaan numpy, kita bisa bikin matrix"""

# outputnya akan ada koma - komanya --> [1,2,3,4]
list_a = [1, 2, 3, 4]
# print(f"list_a = {list_a**2}")  # menggunakan ini, dia tidak bisa di kuadratkan

# outputnya tidak akan ada koma - komanya --> [1 2 3 4]
vector_a = np.array([1, 2, 3, 4])
print(f"vector_a = {vector_a}")
print(f"vector_a pangkat 2 = {vector_a**2}")  # menggunakan ini, dia bisa di kuadratkan
print(f"vector_a dikali 2 = {vector_a*5}")


matrix_b = np.array([(1, 2), (3, 4)])
print(f"Matrix b = \n {matrix_b}")
print(f"Matrix b^2 = \n {matrix_b**2}")

zeros_c = np.zeros((2, 2))
print(f"Zeros c = \n {zeros_c}")  # Matrix sisinya akan 0 semua

ones_d = np.ones((2, 2))
print(f"Ones d = \n {ones_d}")  # Matrix sisinya akan 1 semua

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n {jumlah}")

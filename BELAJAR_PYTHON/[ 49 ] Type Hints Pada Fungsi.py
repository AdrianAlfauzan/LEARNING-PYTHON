'''Type Hints untuk Fungsi'''

# Bentuk standar fungsi yang sudah kita pelajari


'''ini studi kasus, masalah yang harus dibenah ketika ada string di function!
ini hanya contoh saja, maka dari itu kita perlu memakai type hints. '''
# def fungsi(parameter):
#     hasil = parameter**2
#     print(parameter)

# fungsi(1)
# fungsi("adrian")
# fungsi(True)


'''CARA MEMAKAI TYPE HINTS'''

# Type hint adalah penggunaan untuk nanti kita sharing program ke orang
import string
import os
os.system("cls")

def sepuluh_pangkat(argument:int) -> int:
    '''INI FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output
# jika di ubah jadi string,dia akan error karena outputnya harus INTEGER
hasil = sepuluh_pangkat(2)
print(hasil)

def display(argument:string):
    print(argument)
    
display("adrian")

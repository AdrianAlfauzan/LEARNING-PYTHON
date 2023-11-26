'''Mengenali tentang *Args untuk sebuah data'''
'''args adalah singkatan dari arguments'''

# '''Bagaimana kita mau memasukkan banyak data ke dalam fungsi?'''
# '''kita bisa memakai seperti ini'''
def fungsi(nama,tinggi,berat):
    print(f"nama {nama} tinggi {tinggi} berat {berat}")
fungsi("adrian",167,57)

# '''nah, bagaimana agar menjadi simpel?'''
# '''kita pakai data list'''
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"nama {nama} tinggi {tinggi} berat {berat}")
fungsi(["ronaldo",187,87])

# '''di program atas ini kan lebih ribet ya ^_^, nah kita dpt menggunakan
# sebuah *args sebuah parameter yang digunakan dalam definisi fungsi untuk 
# menangani argumen posisional yang dinamis.'''



'''MENGENAL SEBUAH *args'''

def fungsi (*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama {nama} tinggi {tinggi} berat {berat}")
fungsi("Pessiun",120,90)

'''Pertanyaan? apa untung memakai *args?'''
'''dgn ini, kita dpt menambahkan data tanpa harus ada redudansi'''

'''*args tidak harus semestinya memakai *args,bisa kita ubah menjadi
*data,*number,*huruf dll'''

# Studi kasus
def tambah(*data):
    # data tipenya adalah tuple, dan dia bisa di iterasi
    output = 0
    for i in data:
        output += i
    return output
hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")
hasil = tambah(10,15,5)
print(f"Hasil = {hasil}")
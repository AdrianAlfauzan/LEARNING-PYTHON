import datetime

# Multikeys
mahasiswa1 = {
    "nama": "adrian",
    "nim": "3411221020",
    "sks_lulus": 130,
    "beasiswa": True,
    "lahir": datetime.datetime(2003, 6, 18),
}
mahasiswa2 = {
    "nama": "ronaldo",
    "nim": "3411221050",
    "sks_lulus": 130,
    "beasiswa": True,
    "lahir": datetime.datetime(2003, 6, 18),
}
mahasiswa3 = {
    "nama": "pessiun",
    "nim": "3411221088",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2003, 6, 18),
}

data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3,
}

print(f"{'KEY' :<6} {'nama': <17} {'NIM':<8} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
# MAH001 --> ada 6 huruf, maka akan dimasukkan syntax "'KEY':<6"
# < 6 --> rata kiri
# > 6 --> rata kanan
# ^ 6 --> discenter

print("-" * 50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
    print(f"{KEY :<6} {NAMA: <17} {NIM:<8} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

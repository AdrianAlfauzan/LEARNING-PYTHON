# Membuat gabungan area rentang dari angka

# +++++++3------10++++++

inputuser = float(
    input(
        "Masukkan Angka yang bernilai : \n kurang dari 3 \n atau \n lebih besar dari 10 \n :"
    )
)

# ++++++3---------------
# Memeriksa angka kurang dari 3
iskurangdari = inputuser < 3
print("Kurang dari 3 : ", iskurangdari)

# ------------10++++++
islebihdari = inputuser > 10
print("Lebih dari 10 : ", islebihdari)

# ++++++3------10++++++
ishasil = iskurangdari or islebihdari
print("Angka yang anda masukkan : ", ishasil)

print("================")
# ------3++++++10------
# kasus irisan
inputuser = float(
    input(
        "Masukkan Angka yang bernilai : \n lebih dari 3 \n dan \n kurang dari 10 \n :"
    )
)
# -------3+++++++
# Memeriksa angka lebih dari 3
islebihdari = inputuser > 3
print("lebih dari 3 : ", islebihdari)

# +++++++10-------
iskurangdari = inputuser < 10
print("kurang dari 10 : ", iskurangdari)

# ++++++3------10++++++
ishasil = iskurangdari and islebihdari
print("Angka yang anda masukkan : ", ishasil)

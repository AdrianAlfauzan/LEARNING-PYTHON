# from . import scientific  # untuk mengambil file scientific
# from . import basic # untuk mengambil file basic

# jika tidak ingin pakai yang di atas,
# kita bisa loncat ke trik yang bawah
# lebih elegan
# artinya "." foldernya dia (matematika), basic itu dari file matematika dan, import fungsi - fungsinya yang ada di file basic.py
from .basic import tambah, kali

# artinya "." foldernya dia (matematika), scientific itu dari file matematika dan, import fungsi - fungsinya yang ada di file scientific.py
from .scientific import pangkat

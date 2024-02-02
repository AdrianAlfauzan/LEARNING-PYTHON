from . import Operasi

# atau pakai yg dibawah juga bisa
# from CRUD import Operasi

DB_NAME = "D:\\BELAJAR FT MY CODING\\BELAJAR PYTHON\\BELAJAR_PYTHON\\[ 68 ] Init Database_Create_Read_Update_Delete\\CRUD\\Data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "judul": 255 * " ",
    "penulis": 255 * " ",
    "tahun": "yyyy",
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database Telah Tersedia, __init__.py is Done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru : ")
        Operasi.create_first_data()

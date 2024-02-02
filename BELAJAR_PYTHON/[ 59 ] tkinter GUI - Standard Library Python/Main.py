# GUI --> Graphical User Interface
# contohnya --> Vscode

import tkinter as tk  # ini untuk window utamanya

from tkinter import ttk  # ini disebut widget
# Widget --> Fitur yang umumnya digunakan untuk memaksimalkan fungsi sebuah aplikasi di halaman awal
# handphone tanpa harus membuka aplikasi tersebut terlebih dulu.

from tkinter.messagebox import showinfo

# Ini bisa dibilang Init
window = tk.Tk()  # outputnya tidak ada, dia me - looping
window.configure(bg="white")  # untuk background-color
window.geometry("300x200")  # untuk size nya
window.resizable(False, False)  # false untuk X dan False untuk Y
window.title("Program Tkinter")

# Frame input
input_frame = ttk.Frame(window)

# penempatan ada 3 : Grid, Pack , Place
# Disini kita pakai pack, akan berurut dari atas kebawah
input_frame.pack(padx=10, pady=10, fill="x", expand=True)


"""--- KOMPONEN GUI ---"""
# Komponen - komponen
# Input pertama :
# 1. Label nama depan
# Untuk judul menggunakan Label
nama_depan_label = ttk.Label(input_frame, text="Nama depan")
# untuk menampilkan disini memakai pack
nama_depan_label.pack(padx=10, pady=5, fill="x", expand=True)

# 2. Entry nama depan
# untuk input menggunakan Entry
VARIABEL_NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=VARIABEL_NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=5, fill="x", expand=True)

# 3. Label nama belakang
# untuk judul menggunakan Label
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang")
nama_belakang_label.pack(padx=10, pady=5, fill="x", expand=True)

# 4. Entry nama belakang
# untuk input menggunakan Entry
VARIABEL_NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame, textvariable=VARIABEL_NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, pady=5, fill="x", expand=True)


# 5. Membuat fungsi Button ketika di Klik
def VARIABEL_TOMBOL_KLIK():
    print(VARIABEL_NAMA_BELAKANG.get())
    """Fungsi ini akan di panggil oleh tombol"""
    VARIABEL_PESAN = (
        f"Hello {VARIABEL_NAMA_DEPAN.get()} {VARIABEL_NAMA_BELAKANG.get()}!"
    )
    showinfo(title="TITLE SHOW INFO!", message=VARIABEL_PESAN)


# 5. Tombol Button klik
# Untuk button menggunakan Button
VARIABEL_BUTTON = ttk.Button(input_frame, text="Click!", command=VARIABEL_TOMBOL_KLIK)
VARIABEL_BUTTON.pack(padx=10, pady=10, fill="x", expand=True)


# Main loop window
window.mainloop()  # ini juga sama memanggil mainloop() untuk me-looping

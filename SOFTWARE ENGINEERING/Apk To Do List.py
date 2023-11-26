import tkinter as tk
from tkinter import messagebox

# Menyimpan Path File ke dalam Txt
file_path = "D:/BELAJAR FT MY CODING/BELAJAR PYTHON/SOFTWARE ENGINEERING/todolist.txt"

# fungsi untuk menambahkan tugas
def tambah_tugas():
    tugas = entry_tugas.get()
    if tugas :
        listbox_tugas.insert(tk.END,tugas)
        entry_tugas.delete(0,tk.END)
        # simpan tugas ke dalam file txt
        with open(file_path, "a") as file:
            file.write(tugas + "\n")
    else:
        messagebox.showwarning("Silahkan Masukkan tugas!")

# Fungsi untuk menghapus tugas yang kita pilih
def hapus_tugas():
    try:
        index = listbox_tugas.curselection()[0]
        selected_task = listbox_tugas.get(index)
        listbox_tugas.delete(index)

        # hapus tugas dari file txt
        with open(file_path, "r") as file:
            tasks = file.readlines()
        with open(file_path, "w") as file:
            for task in tasks :
                if task.strip() != selected_task.strip():
                    file.write(task)
    except IndexError:
        messagebox.showwarning("Silahkan Pilih tugas yang ingin di hapus!")

# fungsi untuk menutup aplikasi
# root --> untuk menjalankan
def tutup_aplikasi():
    root.destroy()

# Membuat Window Utama
root = tk.Tk()
root.title("Aplikasi To Do List")

# label dan kota inputnya 
label_tugas = tk.Label(root, text="Tambah Tugas : ")
label_tugas.pack()
entry_tugas = tk.Entry(root)
entry_tugas.pack()

# Tombol tambah, selesai dan hapus
tombol_tambah = tk.Button(root, text="Tambah", command=tambah_tugas)
tombol_tambah.pack()

tombol_selesai = tk.Button(root, text="Selesai", command=tutup_aplikasi)
tombol_selesai.pack()

tombol_hapus = tk.Button(root, text="Hapus", command=hapus_tugas)
tombol_hapus.pack()

# Daftar tugas 
listbox_tugas = tk.Listbox(root)
listbox_tugas.pack() # pack adalah isinya

try:
    with open(file_path, "r") as file :
        tasks = file.readlines()
        for task in tasks:
            listbox_tugas.insert(tk.END, task.strip())
except FileNotFoundError:
    pass

# Menjalankan aplikasi
root.mainloop()
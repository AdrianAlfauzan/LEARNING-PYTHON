# data_generator.py

import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk


def generate_and_save_data(num_data_points):
    # Membuat data secara acak dengan jumlah tertentu
    data_acak = [random.uniform(1, 100) for _ in range(num_data_points)]

    # Membuat folder "data" jika belum ada
    if not os.path.exists("data"):
        os.makedirs("data")

    # Menyimpan data ke dalam file "data_file.txt" di dalam folder "data"
    with open(os.path.join("data", "data_file.txt"), "w") as file:
        for item in data_acak:
            file.write(f"{item}\n")


class DataGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Generator App")

        # Menggunakan ThemedTk untuk tema yang lebih menarik
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Frame untuk memuat widget
        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label dan Entry untuk input jumlah data
        self.label = ttk.Label(self.frame, text="Jumlah Data:")
        self.num_data_entry = ttk.Entry(self.frame)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.num_data_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Tombol untuk menghasilkan dan menyimpan data
        self.generate_button = ttk.Button(
            self.frame, text="Generate & Save Data", command=self.generate_and_save
        )
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def generate_and_save(self):
        try:
            num_data_points = int(self.num_data_entry.get())
            generate_and_save_data(num_data_points)
            tk.messagebox.showinfo("Success", "Data berhasil di-generate dan disimpan!")
        except ValueError:
            tk.messagebox.showerror("Error", "Masukkan jumlah data yang valid.")


# Membuat instance dari ThemedTk
root = ThemedTk(
    theme="arc"
)  # Menggunakan tema "arc", Anda dapat menggantinya sesuai keinginan
app = DataGeneratorApp(root)

# Menjalankan aplikasi GUI
root.mainloop()

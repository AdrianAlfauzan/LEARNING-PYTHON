# data_analyzer_gui.py

import os
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from analisis import DataAnalyzer


class DataAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Analyzer App")

        # Frame untuk memuat widget
        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label dan Entry untuk input file
        self.label = ttk.Label(self.frame, text="File Data:")
        self.file_entry = ttk.Entry(self.frame, width=40)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Tombol untuk analisis dan plot
        self.analyze_button = ttk.Button(
            self.frame, text="Analyze", command=self.analyze_data
        )
        self.plot_button = ttk.Button(
            self.frame, text="Plot Data", command=self.plot_data
        )
        self.analyze_button.grid(row=1, column=0, pady=10, sticky=tk.W)
        self.plot_button.grid(row=1, column=1, pady=10, sticky=tk.E)

        # LabelFrame untuk menampilkan hasil analisis
        self.result_frame = ttk.LabelFrame(master, text="Hasil Analisis")
        self.result_frame.grid(
            row=1, column=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S)
        )

        # Treeview untuk menampilkan hasil analisis
        columns = ("Statistik", "Nilai")
        self.result_tree = ttk.Treeview(
            self.result_frame, columns=columns, show="headings", height=4
        )

        for col in columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, width=100, anchor=tk.CENTER)

        self.result_tree.grid(
            row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S)
        )

    def analyze_data(self):
        file_path = self.file_entry.get()
        try:
            with open(file_path, "r") as file:
                data = [float(line.strip()) for line in file]

            # Membuat objek DataAnalyzer dan melakukan analisis data
            analyzer = DataAnalyzer(data)
            mean_value = analyzer.get_mean()
            median_value = analyzer.get_median()
            max_value = analyzer.get_max()
            min_value = analyzer.get_min()

            # Menampilkan hasil analisis pada Treeview
            self.result_tree.insert("", tk.END, values=("Mean", f"{mean_value:.2f}"))
            self.result_tree.insert(
                "", tk.END, values=("Median", f"{median_value:.2f}")
            )
            self.result_tree.insert("", tk.END, values=("Max", f"{max_value:.2f}"))
            self.result_tree.insert("", tk.END, values=("Min", f"{min_value:.2f}"))

            tk.messagebox.showinfo(
                "Hasil Analisis Data", "Analisis data berhasil ditampilkan."
            )

        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File tidak ditemukan.")
        except ValueError:
            tk.messagebox.showerror(
                "Error", "Isi file tidak valid. Pastikan file berisi angka."
            )

    def plot_data(self):
        file_path = self.file_entry.get()
        try:
            with open(file_path, "r") as file:
                data = [float(line.strip()) for line in file]

            # Membuat grafik
            fig = Figure(figsize=(6, 4))
            ax = fig.add_subplot(111)
            ax.plot(data, label="Data")
            ax.set_xlabel("Data Point")
            ax.set_ylabel("Value")
            ax.legend()

            # Menampilkan grafik menggunakan Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File tidak ditemukan.")
        except ValueError:
            tk.messagebox.showerror(
                "Error", "Isi file tidak valid. Pastikan file berisi angka."
            )


# Membuat instance dari tkinter.Tk (root window)
root = tk.Tk()

# Membuat instance dari DataAnalyzerApp
app = DataAnalyzerApp(root)

# Menjalankan aplikasi GUI
root.mainloop()

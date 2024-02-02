import os
import random
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import requests

class DataGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Generator App")

        # Using ThemedTk for a more attractive theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Frame to hold widgets
        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label and Entry for inputting the number of data points
        self.label = ttk.Label(self.frame, text="Jumlah Data:")
        self.num_data_entry = ttk.Entry(self.frame)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.num_data_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Button to generate and save official websites to a file
        self.generate_button = ttk.Button(
            self.frame, text="Generate & Save Official Websites", command=self.generate_and_save_official_websites
        )
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def generate_and_save_official_websites(self):
        try:
            num_websites = int(self.num_data_entry.get())

            # Perform a Google search for websites using PHP
            query = "filetype:php site:google.com"
            api_key = "AIzaSyBSXMpu6lqd8kViIpy1GNWQ1symTXdMRzw"
            cx = "AIzaSyBbbz_doKaXQ_hz4grKdztjesmlkpE9Fh4"
            start_index = 1

            google_results = []

            while len(google_results) < num_websites:
                params = {
                    'q': query,
                    'key': api_key,
                    'cx': cx,
                    'start': start_index
                }

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                response = requests.get('https://www.googleapis.com/customsearch/v1', params=params, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    if 'items' in data:
                        google_results.extend([item['link'] for item in data['items']])
                    else:
                        break
                else:
                    messagebox.showerror("Error", f"Terjadi kesalahan HTTP: {response.status_code}")
                    break

                start_index += 10

            # Save the results to a file
            file_path = os.path.join("GenerateWebPhp", "google_php_websites.txt")
            with open(file_path, "w") as file:
                file.write("\n".join(google_results[:num_websites]))

            messagebox.showinfo("Generated Google PHP Websites", f"Websites PHP dari Google berhasil disimpan ke dalam file:\n{file_path}")
        except ValueError:
            tk.messagebox.showerror("Error", "Masukkan jumlah website yang valid.")

# Create an instance of ThemedTk
root = ThemedTk(theme="arc")  # You can change the theme as desired
app = DataGeneratorApp(root)

# Run the GUI application
root.mainloop()

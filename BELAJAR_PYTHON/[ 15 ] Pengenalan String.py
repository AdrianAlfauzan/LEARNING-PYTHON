data = "Ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
"""1. menggunakan single quote '...'
   2. menggunakan double quote "..."
   quote = ' dan "
   """
data = "menggunakan single quote"
print(data)

data = "menggunakan double quote"
print(data)

# contoh
print('"Halo bruh!"')
print("'Halo bruh!'")
print("Ini adlaah hari jum'at")

# 2. Menggunkan tanda \
# Membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it ?')

# backslash
print("C:\\user\\Ucup") # untuk slash agar menjadi (C:\user\Ucup)

# Tab
print("Ronaldo \t\t Messi, semakin jauh")

# Backspace
print("Ronaldo \bMessi,jadi deketan")

# Newline 
print("Baris pertama. \nBaris kedua.") # LF -> Line Feed (dipakai di Unix,Linux,MacOs)
print("Baris pertama. \rBaris kedua.") # CR -> Carriage Return (dipakai di commodore,acorn,lisp)
print("Baris pertama. \r\nBaris kedua.") # CRLF -> Line feed carriage return (dipakai di Windows)

# 3. String literal atau Raw
# HATI - HATI
print('C:\new Folder') # akan salah pathnya

# Menggunakan raw string
print(r'C:\new Folder') # akan benar pathnya

# Multiline literal String
print("""
Nama : Adrian
Profesi : Programmer
""")

# Multiline literal String dan Raw
print(r"""
Nama : Adrian
Profesi : Programmer
      \normal website
      www.adrian.com
""")

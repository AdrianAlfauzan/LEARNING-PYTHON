import pygame

# Struktur bikin game :
# 1. Init / Inisialisasi --> contoh bikin charakter nya, world nya dll
# --> seperti membuat mobile legends, kita perlu init.
pygame.init()  # ini untuk memulai gamenya / runtimenya

# Membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# Object Game
# Posisi / Koordinatnya
x = 250
y = 250

# Ukuran Kotak di dalam Framenya
panjang = 20
lebar = 20

# Kecepatan gerak / speed
speed = 10

# Variabel Running game
isRun = True
while isRun:
    pygame.time.delay(20)
    # 2. user input, database input
    # --> user input yang kita masukkan , misalkan dari : stick,mouse , keyboard, memasukkan user dan password dll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # Kita akan ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # Ambil ke kiri "Gunakan arah panah keyboard"
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed

    # 3. lalu, kita update object nya, update asset yang ada di gamenya
    # --> Lalu, kita update asset, misalkan di awal itu memasukkan menu dll
    window.fill((255, 255, 255))  # Ini warna putih

    # Membuat kotaknya
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))

    # 4. render ke display
    # --> lalu kita render, ini adalah yang paling berat. ini untuk menentukan FPS nya
    pygame.display.update()  # agar menjadi putih, jadi update assetnya, lalu update displaynya

pygame.quit()

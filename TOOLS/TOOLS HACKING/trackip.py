import socket

hostname = input("Masukan Domain Website :")
ip_address = socket.gethostbyname(hostname)

print(f"Domain Name : {hostname}")
print(f"IP Address : {ip_address}")

import requests

api_key = "YOUR_API_KEY"
phone_number = input("Masukkan Nomor Telepon: ")
api_url = f"https://api.example.com/lookup?phone={phone_number}&apiKey={api_key}"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print(f"Nomor Telepon: {phone_number}")
    print(f"Informasi Tambahan: {data['info']}")
else:
    print("Gagal mengambil informasi.")

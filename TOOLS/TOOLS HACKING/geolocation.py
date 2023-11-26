import requests


def get_location(ip):
    api_key = "YOUR_ACTUAL_IPSTACK_API_KEY"  # Replace with your actual API key
    url = f"http://api.ipstack.com/{ip}?access_key={api_key}"

    response = requests.get(url)
    data = response.json()

    return data


ip_address = input("Masukkan Alamat IP: ")

try:
    location_data = get_location(ip_address)

    if "error" in location_data:
        print("Terjadi kesalahan:", location_data["error"]["info"])
    else:
        print("Informasi Lokasi:")
        print(f"IP Address: {location_data['ip']}")
        print(f"Negara: {location_data['country_name']}")
        print(f"Kota: {location_data['city']}")
        print(
            f"Koordinat: Lat {location_data['latitude']}, Lon {location_data['longitude']}"
        )

except Exception as e:
    print("Terjadi kesalahan:", e)

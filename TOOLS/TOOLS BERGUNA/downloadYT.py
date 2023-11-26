import requests
from urllib.parse import parse_qs, urlparse


def extract_video_id(url):
    query = parse_qs(urlparse(url).query)
    if "v" in query:
        return query["v"][0]
    else:
        raise ValueError("Invalid YouTube URL")


def download_video(video_id, output_path="Download"):
    try:
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        embed_url = f"https://www.youtube.com/embed/{video_id}"

        response = requests.get(embed_url)
        video_title = response.text.split("<title>")[1].split("</title>")[0].strip()

        video_stream_url = f"https://www.youtube.com/get_video_info?video_id={video_id}"
        video_info = requests.get(video_stream_url)

        streams = parse_qs(video_info.text)["url_encoded_fmt_stream_map"]
        video_stream = streams[0].split(",")[0]

        video_data = requests.get(video_stream).content
        file_path = os.path.join(output_path, f"{video_title}.mp4")

        with open(file_path, "wb") as file:
            file.write(video_data)

        print(f"Download selesai! File tersimpan di: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat mendownload: {str(e)}")


# Contoh penggunaan
video_url = input("Masukkan URL video YouTube: ")
video_id = extract_video_id(video_url)
download_video(video_id)

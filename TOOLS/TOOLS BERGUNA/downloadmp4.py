import pytube
import os


def download_mp4(url):
    try:
        youtube = pytube.YouTube(url)
        video_stream = youtube.streams.get_highest_resolution()
        download_folder = "Download"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        file_path = os.path.join(download_folder, video_stream.default_filename)
        video_stream.download(output_path=download_folder)
        os.rename(
            os.path.join(download_folder, video_stream.default_filename), file_path
        )
        print("Download selesai! File tersimpan di:", file_path)
    except Exception as e:
        print("Terjadi kesalahan saat mendownload:", str(e))


# Contoh penggunaan
video_url = input("Masukkan URL video YouTube: ")
download_mp4(video_url)

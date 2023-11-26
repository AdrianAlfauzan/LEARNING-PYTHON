import pytube
import os


def download_mp3(url):
    try:
        youtube = pytube.YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        download_folder = "Download"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        file_path = os.path.join(download_folder, audio_stream.default_filename)
        audio_stream.download(output_path=download_folder)
        os.rename(
            os.path.join(download_folder, audio_stream.default_filename), file_path
        )
        print("Download selesai! File tersimpan di:", file_path)
    except Exception as e:
        print("Terjadi kesalahan saat mendownload:", str(e))


# Contoh penggunaan
video_url = input("Masukkan URL video YouTube: ")
download_mp3(video_url)

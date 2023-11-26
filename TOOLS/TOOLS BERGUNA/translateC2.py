from googletrans import Translator

def translate_to_c2(text):
    # Inisialisasi penerjemah
    translator = Translator()

    # Terjemahkan teks dari bahasa Indonesia ke bahasa Inggris
    translation = translator.translate(text, src='id', dest='en')

    return translation.text

# Meminta pengguna untuk memasukkan teks dalam bahasa Indonesia
while True:
    input_text = input("Masukkan teks dalam bahasa Indonesia: ")

    # Terjemahkan teks menggunakan fungsi translate_to_c2
    translated_text = translate_to_c2(input_text)

    # Tampilkan hasil terjemahan
    print("Teks Terjemahan Bahasa Inggris C2: ", translated_text)

    # Minta pengguna apakah ingin melanjutkan
    lanjutkan = input("Apakah ingin melanjutkan? (ya/tidak): ")
    if lanjutkan.lower() != "ya":
        break

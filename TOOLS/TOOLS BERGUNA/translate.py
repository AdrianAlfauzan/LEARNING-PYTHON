from googletrans import Translator, LANGUAGES


def translate_text(text, source_language, target_language):
    try:
        translator = Translator()
        translated_text = translator.translate(
            text, src=source_language, dest=target_language
        )
        return translated_text.text
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print("Selamat datang ke program penerjemahan teks.")
    text_to_translate = input("Masukkan teks yang ingin Anda terjemahkan: ")

    print("Pilih bahasa sumber:")
    for code, lang in LANGUAGES.items():
        print(f"{code}: {lang}")

    source_language = input("Masukkan kode bahasa sumber: ").strip().lower()

    while source_language not in LANGUAGES:
        print("Bahasa sumber tidak valid. Silakan pilih lagi.")
        source_language = input("Masukkan kode bahasa sumber: ").strip().lower()

    print("Pilih bahasa tujuan:")
    for code, lang in LANGUAGES.items():
        print(f"{code}: {lang}")

    target_language = input("Masukkan kode bahasa tujuan: ").strip().lower()

    while target_language not in LANGUAGES:
        print("Bahasa tujuan tidak valid. Silakan pilih lagi.")
        target_language = input("Masukkan kode bahasa tujuan: ").strip().lower()

    translated_text = translate_text(
        text_to_translate, source_language, target_language
    )
    print(
        f"Terjemahan dari {LANGUAGES[source_language]} ke {LANGUAGES[target_language]}: {translated_text}"
    )

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            else:
                shifted_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)


if __name__ == "__main__":
    text = '''kunci

'''
    shift = 3
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = caesar_decipher(encrypted_text, shift)
    print("Decrypted Text:", decrypted_text)

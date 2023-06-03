def rot13_cipher(text):
    ciphered_text = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                ascii_offset = ord('a')
            else:
                ascii_offset = ord('A')
            shifted_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            ciphered_text += shifted_char
        else:
            ciphered_text += char

    return ciphered_text


def main():
    text = input("Enter the text to encrypt or decrypt: ")

    ciphered_text = rot13_cipher(text)
    print("Ciphered text:", ciphered_text)


if __name__ == '__main__':
    main()

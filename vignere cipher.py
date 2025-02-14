def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

# Get user input
plain_text = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encrypt the plaintext
encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted Text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
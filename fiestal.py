def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def feistel_round(left, right, key):
    new_right = xor(left, key)
    return right, new_right

def feistel_encrypt(plaintext, key, rounds=4):
    assert len(plaintext) % 2 == 0

    half = len(plaintext) // 2
    left, right = plaintext[:half], plaintext[half:]

    for _ in range(rounds):
        left, right = feistel_round(left, right, key)

    return right + left

def feistel_decrypt(ciphertext, key, rounds=4):
    assert len(ciphertext) % 2 == 0

    half = len(ciphertext) // 2
    left, right = ciphertext[:half], ciphertext[half:]

    for _ in range(rounds):
        right, left = feistel_round(right, left, key)

    return left + right

key = b'K3y12345'
plaintext = b"Hello123"

encrypted = feistel_encrypt(plaintext, key)
decrypted = feistel_decrypt(encrypted, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

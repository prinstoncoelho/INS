def caesar_encrypt(message,shift):
    result=""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result+=chr((ord(char)-shift_base+shift)%26 +shift_base)
        else:
            result+= char
    return result
def caesar_decrypt(encrypted_message,shift):
    result=""
    for char in encrypted_message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result+=chr((ord(char)-shift_base-shift)%26 +shift_base)
        else:
            result+=char
    return result
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
encrypted = caesar_encrypt(message, shift)
print("Encrypted:",encrypted)
decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:",decrypted)
                                                
          
          
          

def encryp():
    UpCase="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
    CipherKey="QWERTYUIOPASDFGHJKLZXCVBNM"
    plainT=msg.upper()
    encr=""
    for i in plainT:
        if(i.isalpha()):
            ind=UpCase.index(i)
            encr+=CipherKey[ind]
        else:
            encr+=i
    return encr

def decryp():
    UpCase="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
    CipherKey="QWERTYUIOPASDFGHJKLZXCVBNM"
    decryp=""
    for i in encrypted:
        if(i.isalpha()):
            ind=CipherKey.index(i)
            decryp+=UpCase[ind]
        else:
            decryp+=i
    return decryp
    
    

msg=input("Enter the String: ")
encrypted=encryp()
print("Encrypted: "+encrypted)
decrypted=decryp()
print("Decrypted: "+decrypted)
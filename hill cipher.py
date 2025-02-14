import numpy as np
import math

def text_to_numbers(msg,n):
    while(len(msg)%n != 0):
        msg+="X"
    return [ord(x)-ord("A") for x in msg]

def number_to_text(cipher_num_list):
    return "".join(chr(num+ord("A")) for num in cipher_num_list)

'''def inverrse_matrix(key,n):
    print(np.linalg.inv(np.array(text_to_numbers(key,n)).reshape(n,n)))
    return np.linalg.inv(np.array(text_to_numbers(key,n)).reshape(n,n)).astype(int)'''

def encryption(msg,key):
    n=math.ceil(len(key)**0.5)
    text_matrix=text_to_numbers(msg,n)
    key_matrix=np.array(text_to_numbers(key,n)).reshape(n,n)
    cipher_num_list=[]

    for i in range(0,len(text_matrix),n):
        t_mat=np.array(text_matrix[i:i+n])
        result_matrix=(np.dot(key_matrix,t_mat))%26
        cipher_num_list.extend(result_matrix.tolist())

    return number_to_text(cipher_num_list)

'''def decryption(encrypt,key):
    n=int(len(key)**0.5)
    text_matrix=text_to_numbers(encrypt,n)
    
    inv_key_matrix=inverrse_matrix(key,n)#np.linalg.inv(np.array(text_to_numbers(key)).reshape(kn,kn))
    text_num_list=[]

    for i in range(0,len(text_matrix),n):
        en_mat=np.array(text_matrix[i:i+n])
        result_matrix=(np.dot(inv_key_matrix,en_mat))%26
        text_num_list.extend(result_matrix.tolist())
    print(text_num_list)

    return number_to_text(text_num_list)'''


msg=input("Enter the message: ").upper().replace(" ","")
key=input("Enter the key: ").upper().replace(" ","")
#key="GYBNQKURP"#np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]]) 
encrypt=encryption(msg,key)
print(encrypt)
'''decrypt=decryption(encrypt,key)
print(decrypt)'''
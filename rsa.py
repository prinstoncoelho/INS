def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, msg):
    n = p * q
    phi = (p - 1) * (q - 1)

    for i in range(2, phi):
        if gcd(i, phi) == 1:  # Fixed condition (== instead of =)
            e = i
            break

    j = 0
    while True:
        if (j * e) % phi == 1:  # Fixed condition (== instead of =)
            d = j
            break
        j += 1

    c = (msg ** e) % n
    print("Encrypted message:", c)

    decrypted_msg = (c ** d) % n
    print("Decrypted message:", decrypted_msg)

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
msg = int(input("Enter a message: "))

RSA(p, q, msg)

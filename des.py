import random

s = "HELLO" 

result = ''.join(format(ord(i), '08b') for i in s)

answer = ""
for i in range(len(result)):
    if i % 8 == 0:
        answer += result[i]

l = len(answer) // 2
left = answer[:l]
right = answer[l:]

lt = [2, 3, 6, 7, 1, 6, 5, 9]
keys = []

for i in range(8):
    newKey = ""
    newAnswer = ""

    nl = int(left, 2)
    nl = bin(nl ^ lt[i])  

    nr = int(right, 2)
    nr = bin(nr ^ lt[i])  

    num = 2 + lt[i]
    newKey = nr[num:] + nl[num:]

    rm = []
    while len(rm) < 8:
        r = random.randint(0, len(newKey) - 1)
        if r not in rm:
            rm.append(r)

    for j in range(len(newKey)):
        if j not in rm:
            newAnswer += newKey[j]

    keys.append(newAnswer)

for i in range(len(keys)):
    print("Key", i + 1, "=", keys[i])

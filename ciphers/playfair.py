import numpy as np

key = "MONARCHY".replace('J', 'I')
domain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace('J', 'I')

k = ""

for ch in key + domain:
    if ch not in k:
        k += ch

matrix = np.array(list(k)).reshape(5, 5)

text = input("Plain Text: ").upper().replace('J', 'I').replace(" ", "")

pairs = []
i = 0

while i < len(text):
    a = text[i]

    if i + 1 < len(text):
        b = text[i+1]
    else:
        b = 'X'

    if a == b:
        pairs.append(a + 'X')
        i += 1
    else:
        pairs.append(a + b)
        i += 2

cipher = ""

for p in pairs:
    a, b = p

    r1, c1 = np.where(matrix==a)
    r2, c2 = np.where(matrix==b)

    r1, c1 = r1[0], c1[0]
    r2, c2 = r2[0], c2[0]

    if r1==r2:
        cipher += matrix[r1, (c1+1)%5] + matrix[r2, (c2+1)%5]
    elif c1==c2:
        cipher += matrix[(r1+1)%5, c1] + matrix[(r2+1)%5, c2]
    else:
        cipher += matrix[r1, c2] + matrix[r2, c1]

print(cipher)

pairs.clear()

plain = ""

for i in range(0, len(cipher), 2):
    pairs.append(cipher[i:i+2])

for p in pairs:
    a, b = p

    r1, c1 = np.where(matrix==a)
    r2, c2 = np.where(matrix==b)

    r1, c1 = r1[0], c1[0]
    r2, c2 = r2[0], c2[0]

    if r1==r2:
        plain += matrix[r1, (c1-1)%5] + matrix[r2, (c2-1)%5]
    elif c1==c2:
        plain += matrix[(r1-1)%5, c1] + matrix[(r2-1)%5, c2]
    else:
        plain += matrix[r1, c2] + matrix[r2, c1]

print(plain)
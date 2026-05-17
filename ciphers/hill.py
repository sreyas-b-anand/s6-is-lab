import numpy as np

key = np.array([[3, 3], [2, 5]])

plaintxt = input("Plain Text: ").upper().replace(" ", "")


def encrypt(text):
    cyphertxt = ""

    if len(text) % 2 != 0:
        text += "X"

    for i in range(0, len(text), 2):
        pair = np.array([ord(text[i]) - 65, ord(text[i + 1]) - 65])

        enc = np.dot(key, pair) % 26

        cyphertxt += chr(enc[0] + 65) + chr(enc[1] + 65)

    print(cyphertxt)


encrypt(plaintxt)
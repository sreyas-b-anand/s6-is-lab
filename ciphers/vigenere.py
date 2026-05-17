def vigenere(text, key, mode="encrypt"):
    text = text.upper().replace(" ", "")
    key  = key.upper()
    out = ""

    for i, c in enumerate(text):
        t = ord(c) - 65
        k = ord(key[i % len(key)]) - 65
        out += chr((t + k if mode == "encrypt" else t - k) % 26 + 65)

    return out

msg = input("Enter word: ")
key = input("Enter key : ")

cipher = vigenere(msg, key, mode="encrypt")
plain  = vigenere(cipher, key, mode="decrypt")

print("Ciphertext:", cipher)
print("Decrypted :", plain)
def encrypt(text):
    result = ""
    for char in text:
        result += chr((a * ord(char) + b - 65) % 26 + 65)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(( pow(a, -1, 26) * ord(char) - b - 65) % 26 + 65)
    return result

plain_text = input("Enter Text: ").upper()
a = 3
b = 21
encrypted_text = encrypt(plain_text)

print(f"\nPlain Text: {plain_text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypt(encrypted_text)}")
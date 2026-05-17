def encrypt(text):
    result = ""
    for char in text:
        result += chr((ord(char) + key - 65) % 26 + 65)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr((ord(char) - key - 65) % 26 + 65)
    return result

plain_text = input("Enter Text: ").upper()
key = 3
encrypted_text = encrypt(plain_text)

print(f"\nPlain Text: {plain_text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypt(encrypted_text)}")
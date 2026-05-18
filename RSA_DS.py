from sympy import gcd, mod_inverse, isprime
from hashlib import sha256


def gen_keys():

    phi = (p - 1) * (q - 1)

    e_list = []

    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e_list.append(i)

    print("Possible e values:", e_list)

    e = int(input("Enter an e value from the above list: "))

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return private_key, public_key

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

if not isprime(p) or not isprime(q):
    print("Both p and q must be prime numbers!")
    exit()

n = p * q

private_key, public_key = gen_keys()

e, n = public_key
d, n = private_key

M = input("Enter message: ")

hashed_s = int.from_bytes(
    sha256(M.encode()).digest(),
    byteorder='big'
)

hashed_s = hashed_s % n
print("Hashed message:", hashed_s)

signature = pow(hashed_s, d, n)
print("Signature:", signature)

verified_hash = pow(signature, e, n)
print("Verified hash:", verified_hash)

new_hash = int.from_bytes(
    sha256(M.encode()).digest(),
    byteorder='big'
) % n

if new_hash == verified_hash:
    print("Success: Signature Verified")
else:
    print("Error: Signature Verification Failed")
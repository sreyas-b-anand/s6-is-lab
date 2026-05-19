from sympy import mod_inverse , gcd , isprime


def generate_keys():
    phi = (p-1)*(q-1)

    e_list = []
    for i in range(2 ,  phi):
        if gcd(i, phi) == 1:
            e_list.append(i)


    print(e_list)

    e = int(input("Enter an e value from the above list: "))

    d = mod_inverse(e , phi)

    public_key = (e , n)
    private_key = (d , n)

    return public_key , private_key

def encrypt(M:int , public_key:tuple[int , int]):
    e , n = public_key
    
    cipher = pow(M , e , n) 
    
    return cipher


def decrypt(C:int , private_key:tuple[int , int]):
    d , n = private_key
    
    plain = pow(C , d , n) 
    
    return plain


p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

if not isprime(p) or not isprime(q):
    print("Both p and q must be prime numbers!")
    exit()

n = p * q

public_key , private_key = generate_keys()

M = int(input("Enter message: "))

if M >= n:
    print("Message must be smaller than n")
    exit()
    
cipher = encrypt(M , public_key)
print("Cipher text : " , cipher)
plain = decrypt(cipher , private_key)
print("Plain text : " , plain)

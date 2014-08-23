from mclib import *

def CTR(counter, key):
    ctr = str(bytearray([0] * 8 + [counter] + [0] * 7))
    return encrypt_ECB(ctr, key)

def encrypt_CTR(plaintext, key, nonce=0):
    keystream = ''
    
    while len(keystream) < len(plaintext):
        keystream += CTR(nonce, key)
        nonce += 1
        
    keystream = keystream[:len(plaintext)]
    
    return XOR_ASCII(plaintext, keystream)

def decrypt_CTR(ciphertext, key, nonce=0):
    return encrypt_CTR(ciphertext, key, nonce)

c = Base64ToASCII("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
key = "YELLOW SUBMARINE"

print ba.unhexlify(decrypt_CTR(c, key))


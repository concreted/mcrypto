from mclib import *

def IntToBytestring(val, num_bytes, endianness='big'):
    val = '%x' % val
    if len(val) % 2 != 0:
        val = '0' + val

    result = ba.unhexlify(val)

    if endianness == 'little':
        result = result[::-1]

    result += '\x00' * (num_bytes - len(result))

    return result

def CTR(counter, key, nonce):
    nonce_fmt = IntToBytestring(nonce, 8, 'little')
    ctr_fmt = IntToBytestring(counter, 8, 'little')

    ctr = nonce_fmt + ctr_fmt
    
    return encrypt_ECB(ctr, key)

def encrypt_CTR(plaintext, key, nonce=0):
    keystream = ''
    counter = 0
    while len(keystream) < len(plaintext):
        keystream += CTR(counter, key, nonce)
        counter += 1
        
    keystream = keystream[:len(plaintext)]
    
    return XOR_ASCII(plaintext, keystream)

def decrypt_CTR(ciphertext, key, nonce=0):
    return encrypt_CTR(ciphertext, key, nonce)

c = Base64ToASCII("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
key = "YELLOW SUBMARINE"

print decrypt_CTR(c, key)

from mclib import *

f = open('assets/20.txt', 'r')
plaintexts = [line.strip() for line in f.readlines()]
f.close();

key = generate_AESKey()

ciphertexts = [encrypt_CTR(Base64ToASCII(plaintext), key) for plaintext in plaintexts]

key = ''

# The size of the smallest ciphertext block will be the
# key length. 
key_length = 100000000

for c in ciphertexts:
    if len(c) < key_length:
        key_length = len(c)

print "Key length:",  key_length

# Truncate the ciphertexts to the length of the key. 
# Think of these as the 'blocks' encrypted by a repeating key.
truncated_ciphertexts = [c[:key_length] for c in ciphertexts]

# Make blocks out of the 1st, 2nd, ..., nth chars of each ciphertext 
# block. 
# Think of these as texts XORed with a single char. 
single_letter_blocks = [''.join([c[i] for c in truncated_ciphertexts]) for i in range(key_length)]

# Find the char XORed with each single-letter-XORed block.
key = [find_XOR_SingleChar(block.encode('hex'))[1] for block in single_letter_blocks]

# These chars make up the key.
key = ''.join(key).encode('hex')

print key

for c in truncated_ciphertexts:
    print ba.unhexlify(XOR_Hex(key, c.encode('hex')))



# Matasano Crypto
# 2-9

from mclib import *

f = open("gistfile1_2-10.txt")

buffer = ba.unhexlify(Base64ToHex("".join([line.strip() for line in f])))

key = b"YELLOW SUBMARINE"
iv = chr(0) * 16

p = decrypt_CBC(decrypt_ECB, buffer, key, iv, 16)

print p
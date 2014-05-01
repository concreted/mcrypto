# Matasano Crypto
# 1-7

from mclib import *

f = open("gistfile1_1-7.txt")

buffer = ba.unhexlify(Base64ToHex("".join([line.strip() for line in f])))
print '%r' % buffer[:16]

key = b"YELLOW SUBMARINE"
iv = Random.new().read(AES.block_size)
msg = decrypt_ECB(buffer, key, iv)

#print msg
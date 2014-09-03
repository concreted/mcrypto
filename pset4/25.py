from mclib import *

s = "MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc="

print Base64ToRawBytes(s)



f = open('assets/25.txt', 'r')
c = (Base64ToRawBytes(''.join([line.strip() for line in f])))
#c = ba.unhexlify(Base64ToHex(''.join([line.strip() for line in f])))
#print '%r' % c



key = b"YELLOW SUBMARINE"
iv = Random.new().read(AES.block_size)

p = decrypt_ECB(c, key)

print p


# Matasano Crypto
# 2-16

from mclib import *

block1 = '0000000000000000'
block2 = 'XXXXX.adminxtrue'
input = block1+block2

admin_string = 'XXXXX;admin=true'

c = enc_cbc_bitflip(input)

p = dec_cbc_bitflip(c)

assert combine16(block16(c)) == c

print "User entry in plaintext"
print '%r | %r\n' % (block16(p)[2], block16(p)[3])

dec = ba.unhexlify(XOR_ASCII(block16(c)[2], block2))

attack = ba.unhexlify(XOR_ASCII(dec, admin_string))


modc = c[:32] + attack + c[48:]
print '\n%r\n' % modc
#modc = c[:32] + attack + c[48:]
modp = block16(dec_cbc_bitflip(modc))

print "Result of decrypting modified ciphertext"
print '\n%r\n' % combine16(modp)
print '%r | %r\n' % (modp[2], modp[3])

#print combine16(modp)

result = parse_cbc_bitflip(combine16(modp))

for key in result:
	print '%s: %r' % (key, result[key])
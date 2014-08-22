# Matasano Crypto
# 1-1

from mclib import *
	
base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

hexTo64 = hexToBase64(hex)
backToHex = Base64ToHex(hexTo64)


print "%r\n%r" % (hexTo64, backToHex)
assert hexTo64 == base64
assert backToHex == hex
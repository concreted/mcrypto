# Matasano Crypto
# 2-9

from mclib import *

padded = pad_PKCS7("YELLOW SUBMARINE", 20)

print '%r' % padded

assert padded == "YELLOW SUBMARINE\x04\x04\x04\x04"
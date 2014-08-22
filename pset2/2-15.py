# Matasano Crypto
# 2-15

from mclib import *

#print unpad("ICE ICE BABY\x04\x04\x04\x04")

test("Padding Validation - Good Pad", unpad("ICE ICE BABY\x04\x04\x04\x04"), "ICE ICE BABY", True)

test_exception("Padding Validation - Bad Pad 1", unpad, "ICE ICE BABY\x05\x05\x05\x05", True)

test_exception("Padding Validation - Bad Pad 2", unpad, "ICE ICE BABY\x01\x02\x03\x04", True)
# Matasano Crypto
# 2-11

from mclib import *

c = encryption_oracle("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

print '%r' % c

if detectECB(c):
	print "ECB detected"
else:
	print "ECB-CBC detected"
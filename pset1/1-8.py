# Matasano Crypto
# 1-8

from mclib import *

from Crypto.Cipher import AES
from Crypto import Random

f = open("gistfile1_1-8.txt")

for line in f:
	detectECB(line.strip())



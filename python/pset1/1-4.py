# Matasano Crypto
# 1-4

from mclib import *

f = open("gistfile1_1-4.txt")

print max( [find_XOR_SingleChar(line.strip()) for line in f] , key=lambda x: x[0] )
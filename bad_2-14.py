# Matasano Crypto
# 2-14

from mclib import *

blocksize = 16
results = dict()
found = False
count = 0

while found == False:
	result = inconsistent_encryption_oracle('')
	size = len(result)
	blocks = [result[i:i+blocksize] for i in range(0, size, blocksize)]
	found = False
	
	#print blocks[0]
	if blocks[0] in results:
		found = True
		firstblock = blocks[0]
		print blocks[0]
		print "Tries: %i" % count
	else:
		results[blocks[0]] = ''
	count += 1
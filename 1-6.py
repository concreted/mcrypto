# Matasano Crypto
# 1-6

from mclib import *

f = open("gistfile1_1-6.txt")

buffer = ba.unhexlify(Base64ToHex("".join([line.strip() for line in f])))
#print buffer
size = len(buffer)

distances = []

for keysize in range(2, 41):
	nhd_1 = hammingDistance(buffer[:keysize], buffer[keysize:keysize+keysize]) / float(keysize)
	nhd_2 = hammingDistance(buffer[keysize*2:keysize*3], buffer[keysize*3:keysize*4]) / float(keysize)
	distances.append( (keysize, (nhd_1+nhd_2) / 2) )
	
distances.sort(key=lambda x: x[1])
distances = distances[:10]
print distances

close_distances = [x[0] for x in distances]

best = ""
score = 0

for n in close_distances:
	keysize_blocks = [buffer[i:i+n] for i in range(0, size, n)]
	blocksize = n
	transposed_blocks = [[]] * blocksize
	result = []

	for i in range(blocksize):
		try:
			transposed_blocks[i] = ''.join([x[i] for x in keysize_blocks])
		except:
			transposed_blocks[i] = ''.join([x[i] for x in keysize_blocks[:-1]])
		result.append(find_XOR_SingleChar(ba.hexlify(transposed_blocks[i])))
		
	score_sum = 0
	for metric, keyChar, ptext, ctext in result:
		score_sum = score_sum + alphaMetric(ptext)
	score_norm = score_sum / n
	
	if score_norm > score:
		score = score_norm
		best = "".join([x[1] for x in result])
		
print best
print ba.unhexlify(XOR_RepeatingKey(buffer, best))
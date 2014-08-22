# Matasano Crypto
# 2-12

from mclib import *

input = ""

base_length = len(consistent_encryption_oracle(input))
length = base_length

while length == base_length:
	input = input + 'A'
	length = len(consistent_encryption_oracle(input))
	
blocksize = length - base_length
print "Block size: %i" % blocksize

print detectECB(consistent_encryption_oracle("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))


attack_input = 'A' * 15

answer = ""

# Find first 16 chars
'''
while len(answer) < 16:
	dictionary = dict()

	for i in range(128):
		plain_char = chr(i)
		crypt_block = consistent_encryption_oracle(attack_input + answer + plain_char)[:16]
		dictionary[crypt_block] = plain_char

	c_block = consistent_encryption_oracle(attack_input)[:16]
	answerChar = dictionary[c_block]
	
	answer = answer + answerChar
	print answer
	
	attack_input = attack_input[:len(attack_input) - 1]
'''

# Find all chars

current_block = 1

while True:
	dictionary = dict()

	for i in range(128):
		plain_char = chr(i)
		#print attack_input + answer + plain_char
		
		crypt_block = consistent_encryption_oracle(attack_input + answer + plain_char)[16 * (current_block - 1):16 * current_block]
		dictionary[crypt_block] = plain_char

	c_block = consistent_encryption_oracle(attack_input)[16 * (current_block - 1):16 * current_block]
	#print c_block
	
	try:
		answerChar = dictionary[c_block]
		
		answer = answer + answerChar

		
		if len(answer) % 16 == 0:
			#print answer
			attack_input = 'A' * 15
			current_block += 1

		else:
			attack_input = attack_input[1:]

	except:
		break

print answer


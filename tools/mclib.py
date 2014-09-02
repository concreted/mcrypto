import sys
import binascii as ba
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random.random import randint

# hexToBase64(string s)
# Convert hex string to base 64 without leading/trailing whitespace.
def hexToBase64(s):
	return ba.b2a_base64(ba.unhexlify(s)).strip()
	
# Base64ToHex(string s)
# Convert base 64 string to hex without leading/trailing whitespace.
def Base64ToHex(s):
	return ba.hexlify(Base64ToASCII(s))

def Base64ToASCII(s):
	return ba.a2b_base64(s).strip()
	
# ASCIIToBinary(string s)
# Convert ASCII string to binary (left-padded to 8 digits).
def ASCIIToBinary(s):
	return "".join([(bin(ord(c))[2:]).zfill(8) for c in s])
	
# XOR_Hex(string x, string y)
# XOR two equal-length hex strings together. Returns hex value.
def XOR_Hex(x, y):
	assert len(x) == len(y)

	return ba.hexlify(XOR_ASCII(ba.unhexlify(x), ba.unhexlify(y)))
	
# XOR_ASCII(string x, string y)
# XOR two ASCII strings together. Returns a string.
def XOR_ASCII(x, y):
	assert len(x) == len(y)

	return str(bytearray([ord(a) ^ ord(b) for a, b in zip(x, y)]))
	
# XOR_SingleChar(string ciphertext, int charascii_dec)
# XOR a hex string with a single char (ASCII decimal value)
def XOR_SingleChar(ciphertext, charascii_dec):
	singleChar = '%02x' % charascii_dec
	cipher = singleChar * (len(ciphertext)/2)
	
	return ba.unhexlify(XOR_Hex(cipher, ciphertext))
	
# XOR_RepeatingKey(string plaintext, string key)
# XOR an ASCII string plaintext with a short ASCII key.
# repeating the key to match length of plaintext.
def XOR_RepeatingKey(plaintext, key):
	size = len(plaintext)
	keysize = len(key)
	cipher = (key * (size/keysize)) + key[:size%keysize]
	
	return XOR_ASCII(plaintext, cipher)

# find_XOR_SingleChar(string ciphertext)
# XOR ciphertext with all 128 normal ASCII chars, 
# to find result most likely to be plain English.
# Return best candidate ASCII char, and XOR result.
def find_XOR_SingleChar(ciphertext):
	return max( map( lambda x: (alphaMetric(x[1]), chr(x[0]), x[1], x[2]), [ (i, XOR_SingleChar(ciphertext, i), ciphertext) for i in range(256) ] ) , key=lambda x: x[0] )
	
# hammingDistance(string a, string b)
# Calculate bitwise Hamming Distance of two ASCII strings.
def hammingDistance(a, b):
	diff = abs(len(a) - len(b))

	return sum(x != y for x, y in zip(ASCIIToBinary(a), ASCIIToBinary(b))) + diff
	
# alphaMetric(string plaintext)
# Calculate metric (between 0 and 1) of how likely given plaintext is 
# normal English text.
def alphaMetric(plaintext):
	score = 0.0
	plaintext_size = len(plaintext)
	plaintext_lowercase = plaintext.lower()
	
	for i in range(0, plaintext_size): 
		char_ascii_val = ord(plaintext_lowercase[i])
		
		if (char_ascii_val >= 97 and char_ascii_val <= 122) or (char_ascii_val == 32):
			score = score + 1.0
		
	return score/plaintext_size
	
# listMatchCount(any item, list l)
# Return number of occurrences of item in list l.
def listMatchCount(item, l):
	return sum(x == item for x in l)
	
# detectECB(string ciphertext)
# Detect ECB encryption in given ciphertext. Return True or False.
def detectECB(ciphertext):
	n = 16
	size = len(ciphertext)
	blocks = [ciphertext[i:i+n] for i in range(0, size, n)]
	duplicates = max(listMatchCount(x, blocks) for x in blocks)
	if duplicates > 2:
		#print "ECB detected - max %i duplicates\n" % duplicates
		#print ciphertext
		#print blocks
		return True
	return False
	
# pad_PKCS7(string block, int size)
# Pad block to length of given size per PKCS7 standard
# (padding byte equals number of padding bytes needed)
def pad_PKCS7(block, size):
	diff = size - len(block)
	assert diff >= 0
	if diff == 0:
		diff = 16
	pad = chr(diff) * diff
	return block + pad
	
def pad16(text):
	size = len(text)
	if size % 16 != 0:
		return pad_PKCS7(text, size + 16 - (size % 16))
	return text
	
def unpad(text):
	pad = text[-1]
	if ord(pad) <= 16 and set(text[-ord(pad):]) == set(pad):
		return text[:len(text) - ord(pad)]
	raise Exception("PKCS7 - bad padding")
	
def block16(text):
	blocksize = 16
	size = len(text)
	return [text[i:i+blocksize] for i in range(0, size, blocksize)]
	
def combine16(blocks):
	return "".join([block for block in blocks])
	
# generate_AESKey()
# Generate a random AES key.
def generate_AESKey():
	return Random.new().read(AES.block_size)
	
# encryption_oracle(string input)
# Encrypt input with an unknown key, using either ECB or ECB-CBC. 
def encryption_oracle(input):
	padded_input = Random.new().read(randint(5,10)) + input + Random.new().read(randint(5,10))
	size = len(padded_input)
	padded_input = pad16(padded_input)
	#print len(padded_input)
	#print padded_input
	
	if randint(0,1):
		print "ECB used"
		return encrypt_ECB(padded_input, generate_AESKey(), "")
	else:
		print "ECB-CBC used"
		return encrypt_CBC(encrypt_ECB, padded_input, generate_AESKey(), Random.new().read(AES.block_size), 16)
		
def consistent_encryption_oracle(input):
	padded_input = input + ba.unhexlify(Base64ToHex("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"))
	
	#padded_input = Random.new().read(randint(5,10)) + input + Random.new().read(randint(5,10))
	size = len(padded_input)
	padded_input = pad16(padded_input)
	
	key = 'f\xb9\xb3\x87\rGk\xb7&\xe6\xe3\xb2y\xa4\x04\x07'
	
	return encrypt_ECB(padded_input, key, "")
	
def inconsistent_encryption_oracle(input):
	padded_input = Random.new().read(randint(0,8)) + input + ba.unhexlify(Base64ToHex("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"))
	
	#padded_input = pad16(padded_input)
	
	key = 'f\xb9\xb3\x87\rGk\xb7&\xe6\xe3\xb2y\xa4\x04\x07'
	
	return encrypt_ECB(padded_input, key, "")

	
# decrypt_ECB(ciphertext, key, iv)
# Decrypt given ciphertext with AES-ECB.
def decrypt_ECB(ciphertext, key, iv=""):
	cipher = AES.new(key, AES.MODE_ECB, iv)
	return cipher.decrypt(ciphertext)
	
# encrypt_ECB(plaintext, key, iv)
# Pad plaintext to multiple of 16 length, then
# encrypt given plaintext with AES-ECB.
def encrypt_ECB(plaintext, key, iv=""):
	cipher = AES.new(key, AES.MODE_ECB, iv)
	#return cipher.encrypt(plaintext)
	return cipher.encrypt(pad16(plaintext))
	
# encrypt_CBC(enc_alg, text, key, iv, blocksize)
# Encrypt given text with encryption algorithm enc_alg in CBC mode. 
def encrypt_CBC(enc_alg, text, key, iv="\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", blocksize=16):
	size = len(text)
	blocks = [text[i:i+blocksize] for i in range(0, size, blocksize)]
	blocks[-1] = pad_PKCS7(blocks[-1], blocksize)
	if len(blocks[-1]) == 32:
		padding_block = blocks[-1][16:]
		blocks[-1] = blocks[-1][0:16]
		blocks.append(padding_block)

	text = ba.unhexlify(XOR_ASCII(blocks[0], iv))

	blocks[0] = enc_alg(text, key, iv)
	
	for i in range(1, len(blocks)):
		text = ba.unhexlify(XOR_ASCII(blocks[i], blocks[i-1]))
		blocks[i] = enc_alg(text, key, iv)

	return ''.join(blocks)


	
# decrypt_CBC(dec_alg, text, key, iv, blocksize)
# Decrypt given text with encryption algorithm dec_alg in CBC mode
def decrypt_CBC(dec_alg, text, key, iv="\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", blocksize=16):
	size = len(text)
	result = b""
	orig_blocks = [text[i:i+blocksize] for i in range(0, size, blocksize)]
	blocks = [''] * len(orig_blocks)
	
	for i in range (len(orig_blocks)):
		blocks[i] = dec_alg(orig_blocks[i], key, iv)
		if i == 0:
			blocks[i] = ba.unhexlify(XOR_ASCII(blocks[i], iv))
		else:
			blocks[i] = ba.unhexlify(XOR_ASCII(blocks[i], orig_blocks[i-1]))

	return ''.join(blocks)
	
# parse_cookie(string cookie):
# Parse given cookie in format "key1=val1&key2=val2&..."
# to { key1: val1, key2: val2, ... }
def parse_cookie(cookie):
	return { key:value for key, value in [item.split('=') for item in cookie.split('&')] } 
	
def profile_for(email):
	key = '\x11\xa9D\x9ap\x86 h(a@\xd1\xc9\xeb7\x95'
	
	profile = "email=%s&uid=10&role=user" % email.replace('&', '').replace('=','')
	#profile = "%s&uid=10&role=user" % email
	
	ciphertext = encrypt_ECB(profile, key)
	
	return ciphertext
	
def find_appended(function, prefix="", block_size=16):
	offset = block_size - len(prefix)
	attack_size = offset - 1
	
	attack_input = 'A' * attack_size

	answer = ""

	current_block = 1

	while True:
		dictionary = dict()

		for i in range(128):
			plain_char = chr(i)
			
			crypt_block = function(attack_input + answer + plain_char)[16 * (current_block - 1):16 * current_block]
			dictionary[crypt_block] = plain_char

		c_block = function(attack_input)[16 * (current_block - 1):16 * current_block]
		#print c_block
		
		try:
			answerChar = dictionary[c_block]
			
			answer = answer + answerChar
			sys.stdout.write(answerChar)
			
			
			if len(answer) % offset == 0:
				#print answer
				attack_input = 'A' * (block_size - 1)
				current_block += 1
				#raw_input()
			else:
				attack_input = attack_input[1:]

		except:
			break
	
	return answer
	
def find_appended_random(function, prefix="", block_size=16):
	# Find block with no appended random bytes (firstblock)
	results = dict()
	found = False
	count = 0

	while found == False:
		result = function('A' * 16)
		size = len(result)
		blocks = [result[i:i+block_size] for i in range(0, size, block_size)]
		found = False
		
		#print blocks[0]
		if blocks[0] in results:
			found = True
			firstblock = blocks[0]
			print firstblock
			print "Tries: %i" % count
		else:
			results[blocks[0]] = ''
		count += 1


	offset = block_size - len(prefix)
	attack_size = offset - 1
	
	attack_input = ('A' * 16) + ('A' * attack_size)

	answer = ""

	current_block = 2
	
	#raw_input()

	# Break with attack input
	# Have to test inputs until get ciphertext with no added random bytes
	while True:
		dictionary = dict()

		for i in range(128):
			plain_char = chr(i)
			
			crypt = function(attack_input + answer + plain_char)
			
			while crypt[:16] != firstblock:
				crypt = function(attack_input + answer + plain_char)
			
			crypt_block = crypt[16 * (current_block - 1):16 * current_block]
			dictionary[crypt_block] = plain_char

		c = function(attack_input)
		while c[:16] != firstblock:
			c = function(attack_input)
			
		c_block = c[16 * (current_block - 1):16 * current_block]

		
		try:
			answerChar = dictionary[c_block]
			
			answer = answer + answerChar
			sys.stdout.write(answerChar)
			
			
			if len(answer) % offset == 0:
				#print answer
				attack_input = ('A' * 16) + ('A' * (block_size - 1))
				current_block += 1
				#raw_input()
			else:
				attack_input = attack_input[1:]

		except:
			break
	
	return answer
	
def enc_cbc_bitflip(input):
	key = 'f\xb9\xb3\x87\rGk\xb7&\xe6\xe3\xb2y\xa4\x04\x07'
	
	prepend = "comment1=cooking%20MCs;userdata="
	append = ";comment2=%20like%20a%20pound%20of%20bacon"
	ptext = "%s%s%s" % (prepend, input.replace(';', '";"').replace('=', '"="'), append)
	
	ptext = pad16(ptext)
	
	return encrypt_CBC(encrypt_ECB, ptext, key)
	
def dec_cbc_bitflip(input):
	key = 'f\xb9\xb3\x87\rGk\xb7&\xe6\xe3\xb2y\xa4\x04\x07'
	
	ptext = decrypt_CBC(decrypt_ECB, input, key)

	return ptext

def parse_cbc_bitflip(ptext):
	items = { key:value for key, value in [item.split('=') for item in ptext.split(';')] } 
	
	if "admin" in items:
		if items["admin"].lower() == 'true':
			print "YOU ARE ADMIN!"
		
	return items

#========== CTR MODE ==========#
def IntToBytestring(val, num_bytes, endianness='big'):
    val = '%x' % val
    if len(val) % 2 != 0:
        val = '0' + val

    result = ba.unhexlify(val)

    if endianness == 'little':
        result = result[::-1]

    result += '\x00' * (num_bytes - len(result))

    return result

def CTR(counter, key, nonce):
    nonce_fmt = IntToBytestring(nonce, 8, 'little')
    ctr_fmt = IntToBytestring(counter, 8, 'little')

    ctr = nonce_fmt + ctr_fmt
    
    return encrypt_ECB(ctr, key)

def encrypt_CTR(plaintext, key, nonce=0):
    keystream = ''
    counter = 0
    while len(keystream) < len(plaintext):
        keystream += CTR(counter, key, nonce)
        counter += 1
        
    keystream = keystream[:len(plaintext)]
    
    return XOR_ASCII(plaintext, keystream)

def decrypt_CTR(ciphertext, key, nonce=0):
    return encrypt_CTR(ciphertext, key, nonce)	


#========= PRNGs ==========#

class MersenneTwister:
    def __init__(self, seed):
        self.MT = [0] * 624
        self.index = 0

        self.initialize_generator(seed)

    def lowest_32_bits_of(self, n):
        return int(n % 2**32)

    def initialize_generator(self, seed):
        # Handle >32bit seed:
        if seed > 2**32:
            seed = self.lowest_32_bits_of(seed)

        self.index = 0
        self.MT[0] = seed

        for i in range(1, 624):
            self.MT[i] = self.lowest_32_bits_of(1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i)

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()

        y = self.MT[self.index]

        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 2636928640)
        y = y ^ ((y << 15) & 4022730752)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        
        return y

    def generate_numbers(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i+1) % 624] & 0x7fffffff)
            self.MT[i] = self.MT[(i+397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] = self.MT[i] ^ 2567483615

		
class MTStreamCipher:
    def __init__(self, seed16):
        self.seed = seed16 % 2**16
        self.generator = MersenneTwister(self.seed)

    def reseed(self, seed16):
        self.seed = seed16 % 2**16
        
    def encrypt(self, plaintext):
        self.generator.initialize_generator(self.seed)
        keystream = ''
        while len(keystream) < len(plaintext):
            rn = self.generator.extract_number()

            bin_rn = bin(rn)[2:]

            while len(bin_rn) > 0:
                char = chr(int(bin_rn[:8], 2))
                bin_rn = bin_rn[8:]
                keystream += char
            
        keystream = keystream[:len(plaintext)]

        return XOR_ASCII(keystream, plaintext)

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)


	
#=========TEST FUNCTIONS=========#

def test(label, output, expected, verbose=False):
	if output == expected:
		if verbose:
			print 'PASSED: %s\n%r == %r\n' % (label, output, expected)
		return True
	print 'FAILED: %s\n%r != %r\n' % (label, output, expected)
	return False
	
def test_exception(label, function, input, verbose=False):
	try:
		function(input)
		print 'FAILED: %s did not throw exception\n' % (label)
		return False
	except:
		if verbose:
			print 'PASSED: %s threw exception\nInput: %r\n' % (label, input)
		return True

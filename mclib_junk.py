# singleCharXORFast(string s)
# Find single character used to XOR a hex string 
# (assumed to be English plaintext). 
# ===============================================
# Fast version:
# Finds most common character c and XORs ptext with c XOR 'e'. 
def singleCharXORFast(s):
	#print s	
	ptext = s
	s = ba.unhexlify(s)
	most = 0
	char = ""
	while len(s) > 0:	
		count = s.count(s[0])
		if count > most:
			most = count
			char = s[0]
		s = s.replace(s[0], "")
	#print most, char
	common = int(ba.hexlify(char), 16)

	cipherChar = common ^ 101

	
	return singleCharXOR(ptext, cipherChar)

# letterCount(string s)
# Returns list of (letter, count) pairs sorted by count.
def letterCount(s):
	counts = []
	while len(s) > 0:
		if s[0].isalpha():
			counts.append( (s[0], s.count(s[0])) )
		s = s.replace(s[0], "")
	counts.sort(key=lambda x: x[1], reverse=True)
	return counts
	
# ptextMetrics(string s)
# Calculates how close letter frequency in s is to English standard letter frequency
# Doesn't really work?
def englishMetric(s):
	ref = "etaoinshrdlcumwfgypbvkjxqz"
	charFreq = ''.join(x[0] for x in letterCount(s))
	print charFreq
	return hammingDistance(charFreq, ref[:len(charFreq)])
	
	
	
#print Base64ToHex('AAAA')
#print "%r" % pad_PKCS7("YELLOW SUBMARIN", 20)
#text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#key = b"YELLOW SUBMARINE"
#iv = chr(0) * 16
#print encrypt_ECB_CBC(text, key, iv)
#c = encrypt_CBC(encrypt_ECB, text, key, iv, 16)
#d = encrypt_CBC(decrypt_ECB, c, key, iv, 16)

'''
print '%r' % c[:16]

print '%r' % encrypt_ECB(text[:16], key, iv)
print '%r' % encrypt_ECB(ba.unhexlify(XOR_ASCII(text[:16], iv)), key, iv)
'''
''' Manual CBC decrypt
print '%r' % decrypt_ECB(c[:16], key, iv)
print '%r' % ba.unhexlify(XOR_ASCII(decrypt_ECB(c[16:32], key, iv), c[:16]))
print '%r' % ba.unhexlify(XOR_ASCII(decrypt_ECB(c[32:48], key, iv), c[16:32]))
'''
#print c
#print decrypt_CBC(decrypt_ECB, c, key, iv, 16)
#print d
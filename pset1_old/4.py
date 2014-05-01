import base64

def hexStrPrettyPrint(hex_string):
	if len(hex_string) % 2 == 0:
		s64 = base64.encodestring(hex_string.decode('hex'))
		return base64.decodestring(s64)
	else:
		return "("

def strXOR(x, y):
	x_int = int(x, 16);
	y_int = int(y, 16);
	
	return "%x" % (x_int ^ y_int);
	
def scorePlaintext(plaintext):
	score = 0.0
	plaintext_size = len(plaintext)
	plaintext_lowercase = plaintext.lower()
	for i in range(0, plaintext_size): 
		char_ascii_val = ord(plaintext_lowercase[i])
		if (char_ascii_val >= 97 and char_ascii_val <= 122) or (char_ascii_val == 32):
			score = score + 1.0
		
	#print score/plaintext_size
	return score/plaintext_size

def decodeSingleCharXOR(x):
	# Length of string is hex-string / 2
	str_length = len(x) / 2;		
	str_array = []
	best_result = ""
	best_key = 0
	best_score = 0.0
	
	for i in range(32, 127):		# Try all readable chars
		xor_string = ("%x" % i) * str_length
		result = hexStrPrettyPrint(strXOR(xor_string, x));
		score = scorePlaintext(result)
		#str_array.append(result)
		
		'''
		if scorePlaintext(result) > 0.6:
			print result
			print scorePlaintext(result)
		'''
		if score > best_score:
			best_score = score
			best_key = i
			best_result = result
	
	return {'key': best_key, 'ptext': best_result, 'score': best_score, 'ctext': x}
	
def detectSingleCharXOR(filename):	
	f = open(filename, 'r')
	best_result = {'score': 0.0}
	for line in f:
		line_result = decodeSingleCharXOR(line)
		'''
		print "Score: " + str(line_result['score'])
		print "Key: " + str(line_result['key'])
		print "PText: " + line_result['ptext']
		print "CText: " + line_result['ctext']
		'''
		if line_result['score'] > best_result['score']:
			best_result = line_result
			
	return best_result
		
	
print detectSingleCharXOR("gistfile1.txt")

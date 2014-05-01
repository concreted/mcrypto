import base64

x = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
y = "334b041de124f73c18011a50e608097ac308ecee501337ec3e100854201d"
z = "7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f"

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
		if ord(plaintext_lowercase[i]) >= 97 and ord(plaintext_lowercase[i]) <= 122:
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
			
	print best_key
	print best_result
	print best_score
	return [best_key, best_result]
	
decodeSingleCharXOR(z)

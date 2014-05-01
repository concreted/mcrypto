x = "1c0111001f010100061a024b53535009181c"
y = "686974207468652062756c6c277320657965"

def strXOR(x, y):
	x_int = int(x, 16);
	y_int = int(y, 16);
	
	return "%x" % (x_int ^ y_int);
	
print strXOR(x, y);
	

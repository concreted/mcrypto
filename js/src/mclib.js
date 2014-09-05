var isHex = function(string) {
    if (string.length % 2 !== 0)
	return false;
    
    // Does hexstring contain only valid hex chars?
    if (/[^0-9a-f]/gi.test(string))
	return false;

    return true;
};

var hexToRawBytes = function(hexstring) {
    return '';
};

var hexToBase64 = function(hexstring) {
    return '';
};
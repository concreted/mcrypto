var stringToHex = function(string) {
    var result = '';
    for (var i = 0; i < string.length; i++) {
	result += (string.charCodeAt(i)).toString(16);
    }
    return result;
}

var isHex = function(string) {
    if (string.length % 2 !== 0)
	return false;
    
    // Does hexstring contain only valid hex chars?
    if (/[^0-9a-f]/gi.test(string))
	return false;

    return true;
};

var hexToString = function(hexstring) {
    if (!isHex(hexstring)) {
	throw "hexToRawBytes: input string is not hex";
    }
    
    var result = '';

    for (var i = 0; i < hexstring.length; i+=2) {
	result += String.fromCharCode(parseInt(hexstring.slice(i, i+2), 16));
    }

    return result;
};

var hexToBase64 = function(hexstring) {
    return btoa(hexToString(hexstring));
};

var base64ToHex = function(base64string) {
    return stringToHex(atob(base64string))
};
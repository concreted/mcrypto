var rawToHex = function(string) {
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

var hexToRaw = function(hexstring) {
    if (!isHex(hexstring)) {
	throw "hexToRaw: input string is not hex";
    }
    
    var result = '';

    for (var i = 0; i < hexstring.length; i+=2) {
	result += String.fromCharCode(parseInt(hexstring.slice(i, i+2), 16));
    }

    return result;
};

var hexToBase64 = function(hexstring) {
    return btoa(hexToRaw(hexstring));
};

var base64ToHex = function(base64string) {
    return rawToHex(atob(base64string))
};


var xorRaw = function(a, b) {
    if (a.length != b.length) {
	throw "xorRaw: non-equal input lengths";
    }

    var result = '';

    for (var i = 0; i < a.length; i++) {
	var xorVal = a.charCodeAt(i) ^ b.charCodeAt(i);
	result += String.fromCharCode(xorVal);
    }

    return result;
};

var xorHex = function(a, b) {
    a = hexToRaw(a);
    b = hexToRaw(b);
    var result = xorRaw(a, b);
    return rawToHex(result);
};

var xorRawSingleChar = function(r, chr) {
    if (chr.length != 1) {
	throw "xorRawSingleChar(r, chr): chr must be single letter";
    }

    var chrBuffer = Array(r.length+1).join(chr);
    console.log(chrBuffer);
    return xorRaw(r, chrBuffer);
};


var scoreAlpha = function(text) {
    var nonAlphaChrs = text.match(/[^\w\s,!;:'"\.]/gi) || [];
    var score = (text.length - nonAlphaChrs.length) / text.length;
    return score;
};
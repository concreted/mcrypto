describe('mclib test suite', function() {
    before(function () {

    });

    describe('Hex operations', function() {
	it("should validate hex strings", function() {
	    expect(isHex('0')).to.be(false);
	    expect(isHex('g')).to.be(false);
	    expect(isHex('gg')).to.be(false);
	    expect(isHex('00 ')).to.be(false);
	    expect(isHex('0f')).to.be(true);
	    expect(isHex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')).to.be(true);
	});

	it("should convert hex to base64", function() {
	    expect(hexToBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')).to.be('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t');
	});


    });

    describe('Base64 operations', function() {
	it("should convert base64 to hex", function() {
	    expect(base64ToHex('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')).to.be('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d');

	});

    });

    describe('XOR', function() {
	it("should XOR two hex strings", function() {
	    expect(xorHex('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')).to.be('746865206b696420646f6e277420706c6179');
	});

	it("should XOR raw strings with single-letter buffer", function(){
	    expect(xorRawSingleChar('AAAA', 'z')).to.be(';;;;');
	});
    });
});
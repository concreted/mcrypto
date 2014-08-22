# Matasano Crypto
# Test Suite

from mclib import *

def testSuite():
	test("Hex -> Base64", hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"), "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
	
	test("Base64 -> Hex", Base64ToHex("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"), "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
	
	test("Fixed Length XOR", XOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"), "746865206b696420646f6e277420706c6179")

	test("Finding Single Char XOR", find_XOR_SingleChar("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")[2], "Cooking MC's like a pound of bacon")
	
	test("Repeating Key XOR", XOR_RepeatingKey("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE"), "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
	
	test("Hamming Distance 37", hammingDistance("this is a test", "wokka wokka!!!"), 37)
	test("Hamming Distance 2", hammingDistance("abc", "abcdr"), 2)	

	test("AES-ECB", decrypt_ECB(ba.unhexlify("091230aade3eb330dbaa4358f88d2a6c"), b"YELLOW SUBMARINE", ""), "I'm back and I'm")
	
	test("PKCS7 Padding", pad_PKCS7("YELLOW SUBMARINE", 20), "YELLOW SUBMARINE\x04\x04\x04\x04")
	
	test("ECB-CBC Decryption", decrypt_CBC(decrypt_ECB, ba.unhexlify("091230aade3eb330dbaa4358f88d2a6cd5cf8355cb6823397ad43906df4344557fc4837693c1a8ee3b40acb2323fad396f4ef50cbf02f853d84873973e430c3053c02a6f8db2ed2708131056df66965b"), "YELLOW SUBMARINE", chr(0) * 16, 16), "I'm back and I'm ringin' the bell \nA rockin' on the mike while the fly girls yel")
	
	test("ECB Detection", detectECB('\xe2\xcfS\xe3<\x7f7bv\x9eO\nx%\x93\x00\xe18\xd7~0,I\xe8\'\xe6\x8ei\x96\'\x9dl\xe18\xd7~0,I\xe8\'\xe6\x8ei\x96\'\x9dl\xe18\xd7~0,I\xe8\'\xe6\x8ei\x96\'\x9dl+\x12\xa0^"y:\x94\xaf\x8e\x0f\xf8\xfbR\x89u1\xb76x\xba8!\x13\x19o%0\xc5.\xee\xb2'), True)
	
	test("Cookie Parsing", str(parse_cookie("foo=bar&baz=qux&zap=zazzle")), "{'foo': 'bar', 'baz': 'qux', 'zap': 'zazzle'}")
	
	test("Padding Validation - Good Pad", unpad("ICE ICE BABY\x04\x04\x04\x04"), "ICE ICE BABY")
	test_exception("Padding Validation - Bad Pad 1", unpad, "ICE ICE BABY\x05\x05\x05\x05")
	test_exception("Padding Validation - Bad Pad 2", unpad, "ICE ICE BABY\x01\x02\x03\x04")
	
	
	
testSuite()
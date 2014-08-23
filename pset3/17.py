from mclib import *

class Generator:
    def __init__(self):
        self.strings = ['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=', \
                        'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=', \
                        'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==', \
                        'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==', \
                        'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl', \
                        'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==', \
                        'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==', \
                        'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=', \
                        'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=', \
                        'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93' \
                       ]

        self.key = generate_AESKey()
        self.iv = chr(0) * 16

    def generate(self):
        # Choose random string
        index = randint(0,len(self.strings)-1)
        chosen = self.strings[0] # pad16(self.strings[index])
        
        ciphertext = encrypt_CBC(encrypt_ECB, chosen, self.key, self.iv, 16)
        
        return (ciphertext, self.iv)

    def decrypt(self, ciphertext):
        plaintext = decrypt_CBC(decrypt_ECB, ciphertext, self.key, self.iv, 16)
        
        # Check padding
        try: 
            unpad(plaintext)
            return True
        except:
            return False


def breakGenerator(ciphertext, iv):
    # Padding oracle attack
    
    #==========FILL ME IN==========#
    pass

g = Generator()
c = g.generate()

print g.decrypt(c[0])                    # Should be True
print g.decrypt('asdfasdfasdfasdf')      # Should be False


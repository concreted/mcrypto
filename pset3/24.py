from mclib import *

class MTStreamCipher:
    def __init__(self, seed16):
        self.seed = seed16 % 2**16
        self.generator = MersenneTwister(self.seed)

    def reseed(self, seed16):
        self.seed = seed16 % 2**16
        
    def encrypt(self, plaintext):
        self.generator.initialize_generator(self.seed)
        keystream = ''
        while len(keystream) < len(plaintext):
            rn = self.generator.extract_number()

            bin_rn = bin(rn)[2:]

            while len(bin_rn) > 0:
                char = chr(int(bin_rn[:8], 2))
                bin_rn = bin_rn[8:]
                keystream += char
            
        keystream = keystream[:len(plaintext)]

        return XOR_ASCII(keystream, plaintext)

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)

text = ''.join([chr(randint(0, 255)) for i in range(randint(0, 10))])
text += "a" * 14
print ba.hexlify(text)

mtsc = MTStreamCipher(randint(0, 2**8))

c = mtsc.encrypt(text)
print ba.hexlify(c)

#d = mtsc.decrypt(c)
#print ba.hexlify(d)


# Crack cipher from known plaintext

import time

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'seconds'
        return result
    return f_timer

@timefunc
def crack():
    tester = MTStreamCipher(0)

    for i in range(2**16):
        tester.reseed(i)
        candidate = tester.decrypt(c)
        if candidate == text:
            print "Decrypted:\n" + ba.hexlify(candidate)
            print "Key:", i
            return i

crack()

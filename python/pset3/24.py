from mclib import *

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

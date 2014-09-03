from mclib import *
import time

def generatePWToken():
    signature = 'a' * 14

    cipher = MTStreamCipher(int(time.time()))

    return ba.hexlify(cipher.encrypt(signature))

def tokenIsFromMT19937(token):
    tester = MTStreamCipher(0)
    signature = 'a' * 14

    for i in range(2**16):
        tester.reseed(i)
        candidate = ba.hexlify(tester.encrypt(signature))

        if candidate == token:
            return True
        
    return False

t = generatePWToken()
print t

print tokenIsFromMT19937(t)

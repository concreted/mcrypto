from mclib import *
import time

def crackMTSeed(rn):
    t = int(time.time())
    mt = MersenneTwister(t)
    while True:
        mt.initialize_generator(t)
        current = mt.extract_number()
        if current == rn:
            return t
        t -= 1

mt = MersenneTwister(0)

time.sleep(randint(40, 1000))

mt.initialize_generator(int(time.time()))

time.sleep(randint(40, 1000))

rn = mt.extract_number()
print "Random number:", rn

seed = crackMTSeed(rn)
print "Cracked seed: ", seed

mt.initialize_generator(seed)
print "Output with cracked seed: ", mt.extract_number()


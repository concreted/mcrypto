from mclib import *

mt = MersenneTwister(1)

for i in range(200):
    print mt.extract_number()

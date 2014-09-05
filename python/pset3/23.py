from mclib import *
import math

def temper(n):
    n = n ^ (n >> 11)
    n = n ^ ((n << 7) & 2636928640)
    n = n ^ ((n << 15) & 4022730752)
    n = n ^ (n >> 18)

    return n

def undo_rshift_xor(n, shift):
    n = bin(n)[2:]
    size = len(n)

    result = n[:shift]

    iterations = int(math.ceil(float(size)/shift - 1))

    for i in range(iterations):
        n_block = n[shift*(i+1):shift*(i+2)]
        r_block = result[shift*i:][:len(n_block)]

        blocksize = len(n_block)

        n_block = int(n_block, 2)
        r_block = int(r_block, 2)

        nextblock = bin(n_block ^ r_block)[2:].zfill(blocksize)
        
        result += nextblock

    return int(result, 2)

def undo_lshift_xor(n, shift, mask):
    n = bin(n)[2:].zfill(32)
    size = len(n)

    m = bin(mask >> shift)[2:].zfill(32)

    r = n[-shift:]

    iterations = int(math.ceil(float(size)/shift - 1))
    
    for i in range(iterations):
        n_block = n[-shift * (i+2): -shift * (i+1)]
        r_block = r[-shift * (i+1): len(r) - (shift * (i))]
        m_block = m[ -shift * (i+1): len(m) - (shift * (i))]

        newblock = bin((int(r_block, 2) & int(m_block, 2)) ^ int(n_block, 2))[2:].zfill(shift)

        r = newblock + r

    return int(r, 2)

def untemper(n):
    n = undo_rshift_xor(n, 18)
    n = undo_lshift_xor(n, 15, 4022730752)
    n = undo_lshift_xor(n, 7, 2636928640)
    n = undo_rshift_xor(n, 11)

    return n

mt = MersenneTwister(randint(1, 2**32))

state = []

for i in range(624):
    state.append(mt.extract_number())

state = [untemper(n) for n in state]

copy_mt = MersenneTwister(0)

copy_mt.MT = state

for i in range(1000):
    a = mt.extract_number()
    b = copy_mt.extract_number() 

    if a != b:
        print "Failed!", a, ',', b
        quit()

print "Cloned successfully."
print mt.extract_number()
print copy_mt.extract_number()

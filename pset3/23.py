import math

def temper(n):
    n = n ^ (n >> 11)
    #n = n ^ ((n << 7) & 2636928640)
    #n = n ^ ((n << 15) & 4022730752)
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

        #print "nblock: ", n_block
        #print "rblock: ", r_block

        n_block = int(n_block, 2)
        r_block = int(r_block, 2)

        nextblock = bin(n_block ^ r_block)[2:]
        
        nextblock = nextblock.zfill(blocksize)
        
        #print "block: ", nextblock

        result += nextblock

    return int(result, 2)

def untemper(n):
    n = undo_rshift_xor(n, 18)
    n = undo_rshift_xor(n, 11)

    return n


n = 1234566789

print n
print temper(n)
print untemper(temper(n))


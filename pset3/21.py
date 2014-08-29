from mclib import *

class MersenneTwister:
    def __init__(self, seed):
        self.MT = [0] * 624
        self.index = 0

        self.initialize_generator(seed)

    def lowest_32_bits_of(self, n):
        return int(n % 2**32)

    def initialize_generator(self, seed):
        # Handle >32bit seed:
        if seed > 2**32:
            seed = self.lowest_32_bits_of(seed)

        self.index = 0
        self.MT[0] = seed

        for i in range(1, 624):
            self.MT[i] = self.lowest_32_bits_of(1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i)

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()

        y = self.MT[self.index]

        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 2636928640)
        y = y ^ ((y << 15) & 4022730752)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        
        return y

    def generate_numbers(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i+1) % 624] & 0x7fffffff)
            self.MT[i] = self.MT[(i+397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] = self.MT[i] ^ 2567483615

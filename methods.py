from random import randrange

def gen_methods():
    def increment(byte):
        return byte + 1

    def decrement(byte):
        return byte - 1

    def left_shift(byte):
        return byte << 1
    
    def right_shift(byte):
        return byte >> 1
    
    def compliment(byte):
        return ~byte
    
    def random(byte):
        return randrange(0, 256)

    methods = {
        "increment": increment,
        "decrement": decrement,
        "left_shift": left_shift,
        "right_shift": right_shift,
        "compliment": compliment,
        "random": random
    }

    return methods

METHODS = gen_methods()
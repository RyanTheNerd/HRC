import random
from methods import METHODS

class Byte:
    def __init__(self, addr, method_name):
        self.addr = addr
        self.method_name = method_name

class Patch:
    methods_list = list(METHODS.keys())
    def __init__(self, rom, range, patch_size, method_name = "rand_method"):
        self.enabled = True
        self.size = patch_size
        self.range = range
        self.bytes = []
        self.method_name = method_name
        self.gen_bytes()

    def toggle(self):
        self.enabled = not self.enabled
    def rand_addr(self):
        return random.randrange(self.range[0], self.range[1])

    def get_method(self):
        if(self.method_name == "rand_method"):
            return random.choice(self.methods_list)

        else:
            return self.method_name

    def gen_bytes(self):
        for i in range(self.size):
            self.bytes.append(Byte(self.rand_addr(), self.get_method()))
        

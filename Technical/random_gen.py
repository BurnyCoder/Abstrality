from random import seed
from random import randint


class RandomGen:
    def __init__(self):
        self.seed = seed(randint(0, 1000))
        self.rand_nums = []

    def random_int(self, start, end):
        rand_int = randint(start, end)
        self.rand_nums.append(rand_int)
        return rand_int

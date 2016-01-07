#import numpy as np
class Sphere(object):

    """Docstring for Sphere. """

    def __init__(self):
        """TODO: to be defined1. """
        self.limit_min = -100
        self.limit_max = 100
        self.dim = 30

    def fitness(self, position):
        s = 0.0

        for p in position:
            s += p ** 2

        return s


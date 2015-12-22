#import numpy as np
from math import cos, sqrt

class Griewank(object):

    """Docstring for Griewank. """

    def __init__(self):
        """TODO: to be defined1. """
        self.limit_min = -600
        self.limit_max = 600
        self.dim = 30

    def fitness(self, position):

        """TODO: Docstring for fitness.

        :popl: TODO
        :returns: TODO

        """

        soma = 0
        prod = 1

        for i, posit in enumerate(position, 1):
            soma += (posit ** 2) / 4000
            prod *= cos(posit/sqrt(i))
        
        return soma - prod + 1

        
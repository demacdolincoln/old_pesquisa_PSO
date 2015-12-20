import numpy as np

class Griewank(object):

    """Docstring for Griewank. """

    def __init__(self):
        """TODO: to be defined1. """
        self.limit_min = -600
        self.limit_max = 600
        self.dim = 30

    def fitness(self, popl):
        """TODO: Docstring for fitness.

        :popl: TODO
        :returns: TODO

        """
        for part in popl:
            soma = 0
            prod = 1

            for i, posit in enumerate(part.position, 1):
                soma += (posit ** 2) / 4000
                prod *= np.cos(posit/np.sqrt(i))
            
            part.fitness = soma - prod + 1

            if part.fitness < part.best_fit:
                part.best_fit = part.fitness
                part.best_posit = np.copy(part.position)

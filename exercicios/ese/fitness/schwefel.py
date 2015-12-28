from math import sin, sqrt
class Schwefel(object):

    """Docstring for Sphere. """

    def __init__(self):
        """TODO: to be defined1. """
        self.limit_min = -500
        self.limit_max = 500
        self.dim = 30

    def fitness(self, position):
        d = len(position)
        soma = 0
        for i in position:
            if i < 0:
                soma = soma + sin(sqrt(-i))
            else:
                soma = soma + sin(sqrt(i))

        return (418.982*d)-soma

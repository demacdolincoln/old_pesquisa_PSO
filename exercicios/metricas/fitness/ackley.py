from math import sqrt, cos, exp, pi
class Ackley(object):

    """Docstring for Sphere. """

    def __init__(self):
        """TODO: to be defined1. """
        self.limit_min = -32.768
        self.limit_max = 32.768
        self.dim = 30

    def fitness(self, position):
        d = len(position)
        
        
        a = 20
        b = 0.2
        c = 2*pi
        
        sum1 = 0
        sum2 = 0
        
        for i in position:
            sum1 += i**2
            sum2 += cos(c*i)
            
        term1 = -a * exp(-b*sqrt(sum1/d))
        term2 = -exp(sum2/d)
            
        return term1 + term2 + a + exp(1)

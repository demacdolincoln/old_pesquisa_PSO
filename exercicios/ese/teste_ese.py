from ese import *
from pso_teste_conv import Particle


def teste():
    popl = [Particle(30, 30, 30) for _ in range(10)]
    assert ese(popl) <= 1


def teste2():
    popl = [Particle(3, 30, 30) for _ in range(10)]
    assert ese(popl) >= 0

def teste_omega():
    popl = [Particle(50, 30, 30) for _ in range(10)]
    f = ese(popl)
    assert f <= 1
    assert f >= 0
    omg = omega(f)
    assert omg > 0.4
    assert omg < 0.9

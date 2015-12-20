from fitness.griewank import Griewank as fit
# from scipy.optimize import rosen
from pso import *
from ese import *
from copy import deepcopy

def global_viz(popl, fit, it):
    """TODO: Docstring for global.

    :popl: populacao de particulas
    :fit: objeto fitness
    :it: quantidade de iteracoes

    """
    limit_min = fit.limit_min
    limit_max = fit.limit_max

    popl.sort(key=lambda x: x.best_fit)
    
    gbest = deepcopy(popl[0])

    # valores iniciais do ese
    omg = 0.9
    c1, c2 = 2.0

    for i in range(it):

        # atualiza velocidades
        calc_velocity(popl, gbest, limit_min, limit_max, omg)

        # atualiza posicoes
        calc_posit(popl, limit_min, limit_max)

        # calcula os fitness
        fit.fitness(popl)

        # ordena popl
        popl.sort(key=lambda x: x.best_fit)

        if popl[0].best_fit < gbest.best_fit:
            gbest = deepcopy(popl[0])
        
        # implementacao do ese
        f = ese(popl)
        omg = omega(f)
        c1, c2 = aceleracao(f, c1, c2)

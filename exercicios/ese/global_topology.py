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

    popl_sort = sorted(popl, key=lambda x: x.fitness)[::]
   
    gbest = deepcopy(popl[0])

    # valores iniciais do ese
    omg = 0.8
    c1, c2 = 2.0, 2.0
    
    varss = {'c1':[], 'c2':[], 'omg':[], 'f':[],
            'best_fit':[], 'mean_fit':[], 'sum_veloc':[]}


    for i in range(it):

        # atualiza velocidades
        #calc_velocity(popl_sort, gbest, limit_min, limit_max, omg, c1, c2)

        # atualiza posicoes
        #calc_posit(popl_sort, limit_min, limit_max)
        # calcula os fitness
        for p in popl_sort:
            p.calc_velocity(gbest, limit_min, limit_max, omg, c1, c2)
            p.calc_posit(limit_min, limit_max)
            p.fitness = fit.fitness(p.position)
            _p_best = fit.fitness(p.best_posit)
            if p.fitness < _p_best:
                p.best_fit = p.fitness
                p.best_posit = p.position[::]

        # ordena popl
        popl_sort = sorted(popl_sort, key=lambda x:x.best_fit)[::]

        if popl_sort[0].best_fit < gbest.best_fit:
            gbest = deepcopy(popl_sort[0])

        # implementacao do ese
        f = ese(popl)
        omg = omega(f)
        c1, c2 = aceleracao(f, c1, c2)

        # coleta de dados:
        varss['c1'].append(c1)
        varss['c2'].append(c2)
        varss['omg'].append(omg)
        varss['f'].append(f)
        varss['best_fit'].append(gbest.best_fit)
        varss['mean_fit'].append(sum(i.best_fit for i in popl_sort))
        varss['sum_veloc'].append(sum(popl_sort[0].velocity))

        if i % 100 == 0:
            print(30 * '-')

            print('gbest', gbest)
            print('popl[0]', popl[0])
            print('sum veloc', sum(popl[0].velocity))
            print('c1: ', c1, 'c2: ', c2, 'omega: ', omg, 'f: ', f)
            print('iteracao:', i)
    return varss
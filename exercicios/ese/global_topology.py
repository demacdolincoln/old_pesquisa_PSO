# from scipy.optimize import rosen
from pso import *
from ese import *
from copy import deepcopy
from metricas import *

def global_viz(popl, fit, it):
    """TODO: Docstring for global.

    :popl: populacao de particulas
    :fit: objeto fitness
    :it: quantidade de iteracoes

    """
    limit_min = fit.limit_min
    limit_max = fit.limit_max

    popl_sort = sorted(popl, key=lambda x: x.best_fit)[::]
   
    gbest = deepcopy(popl[0])

    # valores iniciais do ese
    omg = 0.8
    c1, c2 = 2.0, 2.0
    
    #'c1':[], 'c2':[], 'omg':[], 
    varss = {'f':[], 'spacing':[], 'maximum_spread':[],
            'best_fit':[], 'mean_fit':[], 'sum_veloc':[],
            'best_part':[]}


    for i in range(it):

        # atualiza velocidades
        #calc_velocity(popl_sort, gbest, limit_min, limit_max, omg, c1, c2)

        # atualiza posicoes
        #calc_posit(popl_sort, limit_min, limit_max)
        # calcula os fitness
        for p in popl_sort:
            p.calc_velocity(gbest, limit_min, limit_max, omg, c1, c2)
            p.calc_posit(limit_min, limit_max)
            p.calc_fit()

        # ordena popl
        popl_sort = sorted(popl_sort, key=lambda x:x.best_fit)[::]

        # novo gbest
        _cand_gbest = popl_sort[0]
        if _cand_gbest.best_fit < gbest.best_fit:
            gbest = deepcopy(_cand_gbest)

        # implementacao do ese
        f = ese(popl)
        #omg = omega(f)
        #c1, c2 = aceleracao(f, c1, c2)

        # metricas
        varss['maximum_spread'].append(maximum_spread(popl))
        varss['spacing'].append(spacing(popl))

        # coleta de dados:
        #varss['c1'].append(c1)
        #varss['c2'].append(c2)
        #varss['omg'].append(omg)
        varss['f'].append(f)
        varss['best_fit'].append(gbest.best_fit)
        varss['mean_fit'].append(sum(i.best_fit for i in popl_sort))
        varss['sum_veloc'].append(sum(popl_sort[0].velocity))
        varss['best_part'].append(popl_sort[0].fitness)

        # if i % 100 == 0:
        #     print(30 * '-')

        #     print('gbest', gbest)
        #     print('popl[0]', popl[0])
        #     print('sum veloc', sum(popl[0].velocity))
        #     print('c1: ', c1, 'c2: ', c2, 'omega: ', omg, 'f: ', f)
        #     print('iteracao:', i)
    print(fit.__module__.split('.')[1], 'concluido')
    return varss

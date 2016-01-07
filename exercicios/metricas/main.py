from pso import Particle
from global_topology import global_viz as topology
#from topology_2 import global_top as topology

from fitness.griewank import Griewank as g
from fitness.rastring import Rastring as r
from fitness.salomon import Salomon as s
from fitness.ackley import Ackley as a
from fitness.schwefel import Schwefel as sh
from fitness.sphere import Sphere as sp

import csv

list_fits = [sp, r, s, a, sh, g]

for fitness in list_fits:

    # confs iniciais
    iteracoes = 10000
    populacao = 30

    # criando o objeto fitness
    fit = fitness()

    # formacao da populacao inicial
    popl = [Particle(fit) for _ in range(populacao)]


    for i in popl:
        i.fitness = fit.fitness(i.position)
        i.best_fit = i.fitness
        i.best_posit = i.position[::]


    # implementacao de fato 
    data = topology(popl, fit, iteracoes)

    # exportando dados coletados para csv
    file_csv = open('out_metrica_{0}.csv'.format(fit.__module__.split('.')[1]), 'w')
    writer = csv.writer(file_csv)
    writer.writerow(data.keys())
    zz = zip(*data.values())
    for z in zz:
        writer.writerow(z)

    file_csv.close()

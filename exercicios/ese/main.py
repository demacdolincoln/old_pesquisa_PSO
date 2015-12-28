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

list_fits = [g, r, s, a, sh, sp]

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
	file_csv = open('out_{0}_normal.csv'.format(fit.__module__.split('.')[1]), 'w')
	writer = csv.writer(file_csv)
	writer.writerow(data.keys())
	for z in zip(*data.values()):
	    writer.writerow(z)

	file_csv.close()

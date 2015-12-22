from pso import Particle
from global_topology import global_viz
from fitness.griewank import Griewank as fitness
#from fitness.sphere import Sphere as fitness

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
data = global_viz(popl, fit, iteracoes)
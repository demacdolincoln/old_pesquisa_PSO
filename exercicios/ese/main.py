from pso import Particle
from global_topology import global_viz
from fitness.griewank import Griewank as fitness

# confs iniciais
iteracoes = 10000
populacao = 30

# criando o objeto fitness
fit = fitness()

# formacao da populacao inicial
popl = [Particle(fit.dim, fit.limit_min, fit.limit_max) for _ in populacao]

# implementacao de fato 
global_viz(popl, fit, iteracoes)

import numpy as np

class Particle(object):

    """Docstring for Particle. """

    def __init__(self, dim, limit_min, limit_max):
        """TODO: to be defined1.

        :dim: quantidade de dimensoes 
        :limit_min: limite minimo
        :limit_max: limite maximo

        """
        self.velocity = [0] * dim
        self.position = np.random.uniform(limit_min, limit_max, dim)
        self.fitness = None
        self.best_posit = self.position[::]
        self.best_fit = self.fitness

def calc_velocity(popl, gbest, limit_min, limit_max, omega):
    """TODO: Docstring for calc_velocity.

    calculo de velocidade usando o fator de constricao

    :popl: Populacao de particulas
    :gbest: Particula melhor posicionada
    :limit_min: limite minimo
    :limit_max: limite maximo
    :omega: fator de constricao

    """
    for part in popl:
        for index, veloc in enumerate(part.velocity):

            act_posit = part.position[index]
            best_posit = part.best_posit[index]
            gbest_posit = gbest.best_posit[index]

            rnd_0 = np.random.rand() * 2.05
            rnd_1 = np.random.rand() * 2.05

            cognitivo = best_posit - act_posit
            social = gbest_posit - act_posit
            
            new_veloc = omega * (veloc + rnd_0 * cognitivo + rnd_1 * social)

            # controle de valocidade
            if new_veloc > limit_max:
                new_veloc = limit_min
            elif new_veloc < limit_min:
                new_veloc = limit_max

            part.velocity[index] = new_veloc

def calc_posit(popl, limit_min, limit_max):
    """TODO: Docstring for calc_posit

    :popl: populacao de particulas
    :limit_min: limite minimo
    :limit_max: limite maximo

    """
    for part in popl:
        for index, act_posit in enumerate(part.position):
            new_posit = act_posit + part.velocity[index]
            
            if new_posit > limit_max:
                new_posit = limit_max
            elif new_posit < limit_min:
                new_posit = limit_min

            part.position[index] = new_posit

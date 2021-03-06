#import numpy as np
from random import uniform

class Particle(object):

    """Docstring for Particle. """

    def __init__(self,fit): 
        """TODO: to be defined1.

        :dim: quantidade de dimensoes 
        :limit_min: limite minimo
        :limit_max: limite maximo

        """
        self.velocity = [0] * fit.dim
        self.position = [0] * fit.dim
        for i in range(fit.dim):
            self.position[i] = uniform(fit.limit_min, fit.limit_max)
        self.old_position = [0] * fit.dim
        self.fitness = None
        self.best_posit = self.position[::]
        self.best_fit = None
        self._func_fit = fit.fitness

    def __repr__(self):
        return 'fitness: {0} \n best_fit: {1}'.format(self.fitness,self.best_fit)

    def calc_velocity(self, gbest, limit_min, limit_max, omega, c1, c2):
        """TODO: Docstring for calc_velocity.

        calculo de velocidade usando o fator de constricao

        :popl: Populacao de particulas
        :gbest: Particula melhor posicionada
        :limit_min: limite minimo
        :limit_max: limite maximo
        :omega: fator de constricao
        :c1 e c2: fatores de aceleracao

        """

        velocity = []

        for posit in range(len(self.position)):
            inc = self.position[posit]
            veloc = self.velocity[posit]
            cog = self.best_posit[posit]
            soc = gbest.best_posit[posit]

            new_veloc = 0.4*veloc + uniform(0,1)*2.05*(cog - inc) + uniform(0,1)*2.05*(soc - inc)
            #new_veloc = omega*veloc + uniform(0,1)*c2*(cog - inc) + uniform(0,1)*c1*(soc - inc)

            #Controlando a velocidade
            if new_veloc > limit_max:
                new_veloc = limit_min
            elif new_veloc < limit_min:
                new_veloc = limit_max

            velocity.append(new_veloc)

        self.velocity = velocity[::]
    
        # nv = []
        # for index in range(len(self.velocity)):

        #     veloc = self.position[index]
        #     act_posit = self.position[index]
        #     best_posit = self.best_posit[index]
        #     gbest_posit = gbest.best_posit[index]

        #     rnd_0 = uniform(0, 1)
        #     rnd_1 = uniform(0, 1)

        #     #new_veloc = omega* veloc + c1*rnd_0*(best_posit - act_posit) + rnd_1*c2*(gbest_posit - act_posit)
        #     new_veloc = 0.4*veloc + rnd_0*2.05*(best_posit - act_posit) + rnd_1*2.05*(gbest_posit - act_posit)
            
        #     # controle de valocidade
        #     if new_veloc > limit_max:
        #         new_veloc = limit_min
        #     elif new_veloc < limit_min:
        #         new_veloc = limit_max

        #     nv.append(new_veloc)

        # self.velocity = nv[::]

    def calc_posit(self, limit_min, limit_max):
        """TODO: Docstring for calc_posit

        :popl: populacao de particulas
        :limit_min: limite minimo
        :limit_max: limite maximo

        """
		

        self.old_position = self.position[::]
        np = []
        for index in range(len(self.position)):
            new_posit = self.position[index] + self.velocity[index]
            
            if new_posit > limit_max:
                new_posit = limit_max
            elif new_posit < limit_min:
                new_posit = limit_min

            np.append(new_posit)
        
        self.position = np[::]

    def calc_fit(self):
        self.fitness = self._func_fit(self.position)

        if self.fitness < self.best_fit:
            self.best_fit = self.fitness
            self.best_posit = self.position[::]

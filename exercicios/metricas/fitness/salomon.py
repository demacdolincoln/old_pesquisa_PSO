from math import cos, sqrt, pi

class Salomon(object):
	"""docstring for Salomon"""
	def __init__(self):
		self.limit_min = -100
		self.limit_max = 100
		self.dim = 30

	def fitness(self, position):
		a = 1 - cos(2*pi*sqrt(sum([x**2 for x in position]))) 
		b = sum([((x**2)/10) for x in position])

		return a + b
		
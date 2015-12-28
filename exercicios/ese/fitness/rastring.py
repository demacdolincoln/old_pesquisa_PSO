from math import pi, cos

class Rastring(object):
	"""docstring for Rastring"""
	def __init__(self):
		self.limit_min = -5.12
		self.limit_max = 5.12
		self.dim = 30

	def fitness(self, position):
		s = sum([((x**2) - (10*cos(2*pi*x)) + 10) for x in position])
		return s
from math import sqrt

def spacing(popl):
	'''
	S = \sqrt{\frac{1}{1 - n} \sum_{i=1}^n(d - d_i)^2}
	:d: distancia media
	:d_i: distancia de cada particula
	'''

	qnt = len(popl)

	d_i = 0
	d0 = 0
	for i in popl:
		d_i += sum(i.position) 
		d0 += d_i /len(i.position)

	d = d0/qnt

	return sqrt((1/(qnt-1)) * ((d - d_i) ** 2))


def maximum_spread(popl):
	'''
	MS = \sqrt{\sum(max_i - min_i)^2)}
	'''

	sums = 0
	for i in popl:
		ii = i.position
		sums += (min(ii) - max(ii))**2

	return sqrt(sums)
import numpy as np

def ese(popl):
    """
    d_i = 1/(n-1) \sum{ \sqrt{\sum{ (x_i^k - x_j^k)^2}}}

    n = tamanho da populacao

    f = (d_g - d_{min}) / (d_{max} - d_{min})
    """
    n = len(popl)

    # passo 1
    d_is = []
    d_best = None
    for i in popl:
        sum_i = 0
        dist = []
        for j in popl:
            if i != j:
                for d_i, d_j in zip(i.position, j.position):
                    dist.append(np.sqrt((d_i - d_j)**2))
        sum_i = 1/(n-1) * np.sum(dist)
        d_is.append(sum_i)
        if d_best == None:
            d_best = sum_i

    # passo 2
    d_is.sort()
    d_min = d_is[0]
    d_max = d_is[-1]

    f = (d_best - d_min)/(d_max - d_min)

    return f

def omega(f):
    """TODO: Docstring for omega.

    :f: TODO
    :returns: TODO

    """
    omg = 1/(1 + 1.5 * (np.e**(-2.6*f)))

    return omg

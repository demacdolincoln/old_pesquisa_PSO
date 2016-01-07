'''
implementação dos calculo de verificação de estagnação descritos no paper:
Regrouping Particle Swarm Optimization: A New Global Optimization Algorithm with Improved Performance Consistency Across Benchmarks
'''
def Omega(popl):
    """TODO: length of search space - pag 3 do paper

    :popl: populacao de particulas
    :returns: list of calc results

    """
    result = []
    for p in popl:
        r_Omega = []
        for act, old in zip(p.position, p.old_position):
            r_Omega.append(act-old)
        result.append(r_Omega)
	
    return result

def sigma(popl, gbest):
    """
    Swarm Radious - pag 4 do paper

    :popl: populacao de particulas
    :gbest:
    :returns: list of sigma calc results

	"""
    omg = Omega(popl)
    conv = 0
    e = 1.1e-4
    for posit, i in enumerate(omg):
        s = max(map(lambda x: x - gbest.position[posit], i))
        try:
            s_norm = s/abs(sum(i))
        except ZeroDivisionError:
            s_norm = 0
        if s_norm < e:
            conv += 1
    return conv

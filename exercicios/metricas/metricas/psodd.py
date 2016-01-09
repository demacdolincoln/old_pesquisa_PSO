def R(fbest, prev_fbest, mveloc, prev_mveloc):
    """TODO: Docstring for R.
    
    baseado na parte III item 3 (pagina 2) do paper
    A Particle Swarm OPtimization with Stagnation Detection and Dispersion

    :fbest: best fitness atual
    :prev_fbest: best fitness anterior
    :mveloc: media da velocidade de todas as particulas
    :prev_mveloc: velocidade media anterior
    :returns: <int>

    """
    try:
        return abs(1-(fbest/prev_fbest)/ 1-(mveloc/prev_mveloc))
    except ZeroDivisionError:
        return 0

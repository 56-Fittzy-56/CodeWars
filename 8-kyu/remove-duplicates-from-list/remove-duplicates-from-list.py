def distinct(seq):
    resultado = []
    for i in seq:
        if i not in resultado:
            resultado.append(i)
    return resultado
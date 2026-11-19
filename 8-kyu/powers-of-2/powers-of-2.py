def powers_of_two(n):
    lista_resultado = []
    for i in range(0, n+1):
        resultado = 2 ** i
        lista_resultado.append(resultado)
    return lista_resultado
​
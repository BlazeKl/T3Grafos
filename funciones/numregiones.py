#Con el teorema de Euler, determinar la cantidad de regiones
#que tiene el grafo ingresado

# a numero de aristas
# v numero de vertices (es el largo del arreglo, matriz n*n cuadrada)

def cantidad_regiones(a,v):
    if a >= 1 and v >= 2:
        regiones = 2 - v + a
        return regiones
    else:
        return 0
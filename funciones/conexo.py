# x es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos
from numpy.linalg import matrix_power

def is_conexo(x,n):
    arrgl = [[0 for x in range(n)] for y in range(n)]
    matc=[[0 for x in range(n)] for y in range(n)]

    for i in range(0,n):
        for j in range(0,n):
            arrgl[i][j] = x[i][j]
    
    for i in range(0,n):
        matc += matrix_power(arrgl, i) # funcion que eleva la matriz a n y va guardando la sumatoria hasta n
                                        # ej matriz elev 0 + matriz elev 1 + ... + matriz elev n
  #  return matc     #RETORNA UNA MATRIZ C
    is_con = True
    for i in range(0,n):
        for j in range(0,n):
            if matc[i][j] == 0 :
                is_con = False
    
    print("¿El grafo es conexo?")
    if n == 0:
        return False
    return is_con
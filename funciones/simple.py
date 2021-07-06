# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def g_simple(x,n):
    if n==0:
        return False
    else:
        for i in range(0,n):
            for j in range(0,n):
                if i==j: 
                    if x[i][j]==1:
                        return False
        return True    
    

# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def g_completo(x,n):
    if n>=1:
        completo=0
        for i in range(0,n):
            cont=0
            for j in range(0,n):
                if i!=j:
                    if x[i][j]==1:
                        cont+=1
                else:
                    if x[i][j]==1:
                        return False
            if cont==(n-1):
                completo+=1
        if completo==n:
            return True
        else:
            return False
    else:
        return False
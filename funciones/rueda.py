# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def g_rueda(x,n):
    if n>=4:
        tresAristas=0
        central=0
        for i in range(0,n):
            cont=0
            for j in range(0,n):
                if x[i][j]==1:
                    cont+=1
            if cont==3:
                tresAristas+=1
            if cont==(n-1):
                central+=1
        if central==1 and tresAristas==(n-1):
            return True
        else:
            return False
    else:
        return False
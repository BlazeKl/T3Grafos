# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def gradosgrafo(x,n):
    ngrados=0
    for i in range(0,n):
        for j in range(0,n):
            if x[i][j] >= 1:
                ngrados +=1
    return ngrados


# cant_grados= gradosgrafo(x,n)

# cant_aristas= cant_grados / 2
# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def num_cromatico(x,n):
    arrgl = [[0 for x in range(n)] for y in range(n)]
    if n == 0:
        return 0

    for i in range(0,n):
        for j in range(0,n):
            arrgl[i][j] = x[i][j]

    for i in range(0,n):
        for j in range(0,n):
            if arrgl[i][j] != arrgl[j][i]:
                arrgl[i][j] = 1
                arrgl[j][i] = 1
                print("Diff detected")

    mayor=0
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=arrgl[i][j]
        if acum>=mayor:
            mayor=acum    
    return (mayor+1)
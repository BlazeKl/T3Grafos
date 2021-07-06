# x es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada
#n es la cantidad de vertices o nodos



def l_colorear(x,n):
    colors = ["red","blue","green","white","black","orange","navy","dark green","yellow2","brown1","gray50","DodgerBlue4","deep pink","dark green","gold"]
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
    mayor+=1

    arreglo_grados = [0 for x in range(n)]
    arreglo_colores = [0 for x in range(mayor)]
    arreglo_final = [0 for x in range(n)]
    for i in range(0,mayor):
        arreglo_colores[i]=colors[i]
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=arrgl[i][j]
        arreglo_grados[i]=acum

    arreglo_final[0]=colors[0]
    for i in range(1,n):
        cont=0
        for j in range(0,i):
            if arrgl[i][j]==1:
                if arreglo_final[j]==arreglo_colores[cont]:
                    cont+=1
            arreglo_final[i]=arreglo_colores[cont]

    return arreglo_final
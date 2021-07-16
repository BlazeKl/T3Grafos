from .numregiones import cantidad_regiones

def kruskal_tp(x, n):
    y = [[0 for x in range(n)] for y in range(n)]
    cont = 0
    cant_a = 0
    cant_v = 0
    aux = 0
    def f_min(arr, max):
        state = 0
        min = 0
        for i in range(0,n):
            for j in range(0,n):
                if i != j and arr[i][j] != 0 and arr[i][j] > max:
                    if state == 0:
                        min = arr[i][j]
                        state = 1
                    else:
                        if arr[i][j] < min:
                            min = arr[i][j]
        return min

    while(f_min(x, cont) != 0):
        for i in range(0,n):
            for j in range(0,n):
                if x[i][j] == f_min(x, cont) and j > i and x[i][j] != 0 and x[i][j] != y[i][j]:
                    print(chr(96+i),chr(96+j),x[i][j])
                    #arreglo = [chr(96+i),chr(96+j),x[i][j]]
                    cant_a = cant_a + 1
                    bagregari = True
                    bagregarj = True
                    for k in range(0,n):
                        print(k,i)
                        print(k,j)
                        if y[k][j] != 0:
                            bagregari = False
                        if y[k][i] != 0:
                            bagregarj = False
                    if bagregari:
                        cant_v = cant_v + 1
                    if bagregarj:
                        cant_v = cant_v + 1
                    if cantidad_regiones(cant_a, cant_v) <= 1:
                        print("se copia")
                        y[i][j] = x[i][j]
                        y[j][i] = x[i][j]
                    else:
                        print("se crea circuito, undo")
                        cant_a = cant_a - 1
                        if bagregari:
                            cant_v = cant_v - 1
                        if bagregarj:
                            cant_v = cant_v - 1
                    aux = x[i][j]
        cont = aux

    return y
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
        # print(min)
        return min

    # print(f_min(x, 0))
    # print(f_min(x, 7))
    # print(f_min(x, 15))

    while(f_min(x, cont) != 0):
        for i in range(0,n):
            for j in range(0,n):
                if x[i][j] == f_min(x, cont) and j > i and x[i][j] != 0 and x[i][j] != y[i][j]:
                    print(chr(96+i),chr(96+j),x[i][j])
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
                    # if x[i][j] not in y[j]:
                    #     print("1+ vertice")
                    #     cant_v = cant_v + 1
                    # if x[j][j] not in y[i]:
                    #     print("1+ vertice")
                    #     cant_v = cant_v + 1
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
                    # cont = x[i][j]

    # print(f_min(x,0))
    # print(f_min(x,2))
    # while (cont < n):
    #     for i in range(0,n):
    #         for j in range(0,n):
    #             print("min: ",+min)
    #             print("max: ",+max)
    #             print("(",+i,",",+j,")")
    #             print("x[",+i,"][",+j,"]: ", x[i][j])
    #             if x[i][j] <= min and j > i and x[i][j] > max:
    #                 print("encontre algo")
    #                 min = x[i][j]
    #                 vertd[cant_a][0] = i
    #                 vertd[cant_a][1] = j
    #                 cant_a += 1
    #                 if i not in vertd[0]:
    #                     cant_v += 1
    #                 if j not in vertd[1]:
    #                     cant_v += 1
    #                 if 2 - cant_v + cant_a >= 2:
    #                     if i not in vertd[0]:
    #                         cant_v -= 1
    #                     if j not in vertd[1]:
    #                         cant_v -= 1
    #                     vertd[cant_a][0] = 0
    #                     vertd[cant_a][1] = 0
    #                     cant_a -= 1
    #                 max = min
    #     cont += 1

    return y
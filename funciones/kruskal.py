from .numregiones import cantidad_regiones

def kruskal_tp(x, n):
    min = 9999999999999999999999999999999999999999999999999999999999999999999999999
    max = 0
    vertd = [[0 for x in range(n)] for y in range(2)]
    cont = 0
    cant_a = 0
    cant_v = 0
    while (cont < n):
        for i in range(0,n):
            for j in range(0,n):
                if x[i][j] <= min and j > i and x[i][j] > max:
                    min = x[i][j]
                    vertd[cant_a][0] = i
                    vertd[cant_a][1] = j
                    cant_a += 1
                    if i not in vertd[0]:
                        cant_v += 1
                    if j not in vertd[1]:
                        cant_v += 1
        max = min
        cont += 1

    return vertd
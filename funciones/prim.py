
#x : matriz del grafo
#n : cantidad de vertices AKA tamanio matriz
#v_ini : el primer vertice que selecciona el usuario

def prim_tp(x, n, v_ini):
    y = [[0 for x in range(n)] for y in range(n)]
    v_added = [-1 for x in range(n)] #arreglo de vertices pintados
    v_added[0] = v_ini #primer vertice
    print(v_added)
    cont = 0
    contaux=1
    def get_min(arr, pos_y, min_a, state, aux):
        # for i in range(0,n):
        #     print(arr[i])
        for i in range(0,n):
            # print("Vuelta: ",+i)
            if state == 0 and arr[i] != 0 and i not in v_added:
                state = 1
                min_a = arr[i]
                pos_y = i
                print("primer menor: ",+min_a ," en ",chr(97+pos_y))
                aux = aux + 1
            if min_a > arr[i] and arr[i] != 0 and i not in v_added:
                min_a = arr[i]
                pos_y = i
                print("nuevo menor: ",+min_a ," en ",chr(97+pos_y))
                aux = aux + 1
        return min_a, pos_y, min_a, state, aux;

    while cont < n:
        #aqui va codigo para chequear nuevos vertices
        min = 0
        hx = 0       #fila aux
        hy = 0         #columna aux
        state = 0
        min_a = 0
        aux = 0
        for c in range(0,n):  #recorro el arreglo de vertices agregados al arbol
            if v_added[c] != -1:
                print("Buscando: ",chr(97+v_added[c]))
                for i in range(0,n):    #arreglo para recorrer la matriz de peso
                        if i == v_added[c]:
                            print("Encontrado: ",chr(97+v_added[c]))
                            aux2 = aux
                            min, hy, min_a, state, aux= get_min(x[i], hy, min_a, state, aux)
                            if(aux2 != aux):
                                hx = i #Arreglar posicion erronea

        y[hx][hy] = min
        y[hy][hx] = min
        v_added[contaux] = hy
        print(v_added)
        
        contaux= contaux + 1
        
        #contar longitud de arreglo de vertices agregados
        len = 0
        for i in range(0,n):
            if v_added[i] != -1:
                len = len + 1
        print("longitud nueva: ",+len)
        cont = len #largo actual del arreglo v_added

    return y
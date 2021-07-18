#x : matriz del grafo
#n : cantidad de vertices AKA tamanio matriz
#v_ini : el primer vertice que selecciona el usuario

def adyacencia_peso(x, n):
    # -*- coding:utf-8 -*-
# Implementación del algoritmo Kruskal

    def v_a(v_agre,n):
        for i in range(0,n):
             print(v_agre[i])

    def imprimir_v(n):
        for i in range(0,n):
            return chr(97+i)

# Variables globales
    base = dict()
    ord = dict()   

# Función para generar conuntos
    def make_set(v):
        base[v] = v
        ord[v] = 0

    # Implementación de la función de búsqueda 
    # de manera recursiva
    def find(v):
        if base[v] != v:
            base[v] = find(base[v])
        return base[v]

    # Implementación de la unión de conjuntos
    def union(u, v):
        v1 = find(u)
        v2 = find(v)
        if v1 != v2:
            if ord[v1] > ord[v2]:
                base[v2] = v1 
            else:
                base[v1] = v2
                if ord[v1] == ord[v2]: 
                    ord[v2] += 1

    # Función principal del algoritmo Kruskal
    def kruskal(graph):

        # A = {conjunto vacío}
        mst = set()
    
        # Para todo vértice v en G.V
        for v in graph['vertices']:
            make_set(v)
        print ("Sub gráficos creados:")
        print (base)

        # Ordena la lista G.E en forma no decendente por su peso w
        # En este caso usamos el ordenador dentro de python
        edges = list(graph['edges'])
        print(edges)
        edges.sort()
        
        print ("Aristas ordenadas:")
        print (edges)

        # Para toda arista(u,v) en G.E
        for e in edges:
            weight, u, v = e
            # Si encontrar-conjunto(u) != encontrar-conjunto(v)
            if find(u) != find(v):
                # A = A union (u,v)
                union(u, v)
                # Union(u,v)
                mst.add(e)
        return mst 


    v_agregados= ["0" for x in range(1337)]
    
    cont=0

    for i in range(0,n):
        for j in range(0,n):
            if j > i and x[i][j]!=0 :
                arreglo = (x[i][j],chr(97+i),chr(97+j)) # guarda el vertice seleccionado, adyacencia y su peso
                v_agregados[cont]= arreglo              #en formato ['a','b',7], ['a','d',5], ['b','c',8], ['b','d',9], ['b','e',7] 
                cont = cont + 1                                     # etc, buscar imagen grafot3-adyacenciaypeso en carpeta imagen

    

    vertices= ["0" for x in range(n)]

    for i in range(0,n):
        vertices[i]= chr(97+i)
        
    graph = {
    'vertices': vertices,
    'edges':set(v_agregados[i] for i in range(0,cont))

    }

    return kruskal(graph)




# graph = {
# 'vertices': ['a','b','c','d','e','f'],
# 'edges': set([
#     (5,'a','c'),
#     (3,'a','d'),
#     (2,'b','d'),
#     (1,'c','d'),
#     (5,'f','d'),
#     (3,'b','f'),
#     (6,'f','e'),
#     (1,'a','b'),
#     ])
# }

# k = kruskal(graph)
# print "Resultado MST:"
# print k


#     while(f_min(x, cont) != 0):
#         for i in range(0,n):
#             for j in range(0,n):
#                 if x[i][j] == f_min(x, cont) and j > i and x[i][j] != 0 and x[i][j] != y[i][j]:
#                     print(chr(96+i),chr(96+j),x[i][j])
#                     arreglo = [chr(96+i),chr(96+j),x[i][j]]
#                     cant_a = cant_a + 1
#                     bagregari = True
#                     bagregarj = True
#                     for k in range(0,n):
#                         print(k,i)
#                         print(k,j)
#                         if y[k][j] != 0:
#                             bagregari = False
#                         if y[k][i] != 0:
#                             bagregarj = False
#                     if bagregari:
#                         cant_v = cant_v + 1
#                     if bagregarj:
#                         cant_v = cant_v + 1

#                     if cantidad_regiones(cant_a, cant_v) <= 1:
#                         print("se copia")
#                         y[i][j] = x[i][j]
#                         y[j][i] = x[i][j]
#                     else:
#                         print("se crea circuito, undo")
#                         cant_a = cant_a - 1
#                         if bagregari:
#                             cant_v = cant_v - 1
#                         if bagregarj:
#                             cant_v = cant_v - 1
#                     aux = x[i][j]
#         cont = aux








# def prim_tp(x, n, v_ini):
#     y = [[0 for x in range(n)] for y in range(n)]
#     v_added = ["z" for x in range(n)] #arreglo de vertices pintados
#     v_added[0] = v_ini #primer vertice
#     cont = 0
#     # for i in range(0,n):
#     #     for j in range(0,n):
#     #         print()

#     while cont < n:
#         #aqui va codigo para chequear nuevos vertices
#         state = 0   #chequea si es el 1er min encontrado
#         min = 0
#         hx = 0       #fila aux
#         hy = 0         #columna aux
#         for c in range(0,n):  #recorro el arreglo de vertices agregados al arbol
#             if v_added[c] != "z":
#                 for i in range(0,n):    #arreglo para recorrer la matriz de peso
#                     for j in range(0,n):    #arreglo para recorrer la matriz de peso
#                         if j > i and j == c and j not in v_added:
#                             if state == 0:
#                                 min = amin(x[j])
#                                 hx = i
#                                 hy = j
#                             elif min > amin(x[j]):
#                                 min = amin(x[j])
#                                 hx = i
#                                 hy = j
#         y[hx][hy] = min
#         #contar longitud de arreglo de vertices agregados
#         len = 0
#         for i in range(0,n):
#             if v_added[i] != "z":
#                 len = len + 1
#         cont = len #largo actual del arreglo v_added

#     return y
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
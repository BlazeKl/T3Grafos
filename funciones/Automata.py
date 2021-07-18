# -*- coding:utf-8 -*-
# GPL v.3+
# 2015

import graphviz as gv

# Todos los parámetros son listas o tuplas
# donde:
#  * alfabeto:  es el alfabeto aceptado por el 
#               autómata.
#  * estados:   es una lista de estados aceptados
#               por el autómata.
#  * inicio:    Son los estados de inicio del fsm.
#  * trans:     Es una tupla de funciones de transición
#               con tres elementos que son: (a,b,c) donde
#               (a,b) son los estados de partida y llegada;
#               mientras que c es la letra que acepta.
#  * final      Son los estados finales del autómata.

def draw(alfabeto, estados, inicio, trans, final):
    print("inicio:", str(inicio))
    g = gv.Digraph(format='svg')
    g.graph_attr['rankdir'] = 'LR'
    g.node('ini', shape="point")
    for e in estados:
        if e in final:
            g.node(e, shape="doublecircle")
        else:
            g.node(e)
        if e in inicio:
            g.edge('ini',e)

    for t in trans:
        if t[2] not in alfabeto:
            return 0
        g.edge(t[0], t[1], label=str(t[2]))
    g.render(view=True)

# Ejemplo de uso

# if __name__ == '__main__':
#     estados = ["A","B","C","E","F"]
#     trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
#     inicial = ["A"]
#     alf = [0,1]
#     terminal = ("C",)

#     draw(alf, estados, inicial, trans, terminal)

# Ingreso de estados
print ("Ingrese Cantidad de Estados: ");
cant_estados=int(input())
estados=[]
for i in range(1,cant_estados+1):
    nuevoEstado=input("Ingrese Estado N°{}: ".format(i))
    nuevoEstado=nuevoEstado.upper()
    estados.append(nuevoEstado)

# Ingreso del Alfabeto
cant_Alf=int(input("Ingrese la cantidad de Alfabeto: "))
alf=[]
for i in range(0,cant_Alf):
    
    nuevoAlf=input("Ingrese Alfabeto N°{}: ".format(i))
    alf.append(nuevoAlf)

for i in range(0,cant_estados):
    print(estados[i])

# Crear las Transiciones
contador=0;
trans=[]
while(True):
    elemen=[]
    i=1
    while(True):
        trans_1=input("Ingrese Elemento {}: ".format(i))
        trans_1=trans_1.upper()
        if trans_1 in estados:
            break
        else:
            print("Elemento Invalido ")
    i=i+1
    while(True):
        trans_2=input("Ingrese Elemento{}: ".format(i))
        trans_2=trans_2.upper()
        if trans_2 in estados:
            break
        else:
            print("Elemento Invalido ")

    while(True):
        alfa=input("Ingrese Elemento de Alfabeto: ")
        if alfa in alf:
            break
        else:
            print("Alfabeto Invalido ")
    
    elemen.append(trans_1)
    elemen.append(trans_2)
    elemen.append(alfa)
    trans.append(elemen)
    contador=contador+1;
    sig=[0,1]
    while(True):
        siguiente=int(input("0=si\n1=no\n Desea agregar otra transición?: "))
        if siguiente in sig:
            break
        else:
            print("Opción Invalida ")

    if siguiente==1:
        break
# Mostrar las Transiciones
# for i in range(0,contador):
#     print(trans[1])

#Ingreso de Inicial 
inicial=[]    
while(True):
    nuevoInicial=input("Ingrese Inicial N°: ")
    nuevoInicial=nuevoInicial.upper()
    if nuevoInicial in estados:
        break
    else:
        print("Elemento Invalido ")

inicial.append(nuevoInicial)

# Ingreso de Terminales
cant_Terminal=int(input("Ingrese Cantidad de Terminales: "))
terminal=[]
for i in range(1,cant_Terminal+1):
    
    nuevoTerminal=input("Ingrese Terminal N°{}: ".format(i))
    nuevoTerminal=nuevoTerminal.upper()
    terminal.append(nuevoTerminal)

# if __name__ == '__main__':
#     # estados = ["A","B","C","E","F","H"]
#     # trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1),("H","C",0)]
#     # inicial = ["A"]
#     # alf = [0,1]
#     # terminal = ("Q2","Q5")

draw(alf, estados, inicial, trans, terminal)




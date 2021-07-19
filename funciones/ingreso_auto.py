

# Ejemplo de uso ingreso datos automata AFD/AFND para dibujar

# if name == 'main':
#     estados = ["A","B","C","E","F"]
#     trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
#     inicial = ["A"]
#     alf = [0,1]
#     terminal = ("C",)

#     draw(alf, estados, inicial, trans, terminal)


# supongamos que el profe ingresa por pantalla los datos de 2 automatas, independiente de si
# los automatas son: 2 AFD , 2 AFND o 1 AFD y 1 AFND (mixtos)

# print ("ingrese tipo de automata 1")
# nom_automata1 = input()

# print ("ingrese tipo de automata 2")
# nom_automata2 = input()


# #estados automata 1

# print("estados del automata 1")

# print ("ingrese cantidad de estados del automata 1 :")
# cant_est_auto1 = int(input())

# estados1= ["a" for x in range(cant_est_auto1)]

# for i in range(0,cant_est_auto1):
#     print("ingrese estado ", (i + 1),": ")
#     a = input()
#     estados1[i] = a

# #transiciones automata 1

# print("transiciones del automata 1")

# print("ingrese cantidad de transiciones del automata 1 :")
# cant_trans1= int(input())

# trans1= ["a" for x in range(cant_trans1)]

# for i in range(0,cant_trans1):
#     print("ingrese transicion ", (i + 1),": " )
#     a = input()
#     trans1[i] = a

# #alfabeto automata 1

# print("alfabeto del automata 1")

# print("ingrese tamaño del alfabeto del automata 1 : ")
# cant_alf1= int(input())

# alf1= ["a" for x in range(cant_alf1)]

# for i in range(0,cant_alf1):
#     print("ingrese alfabeto ", (i + 1),": " )
#     a = input()
#     alf1[i] = a

# #terminal automata 1

# print("terminal del automata 1")

# print("ingrese cantidad de estados terminales del automata 1 : ")
# cant_ter1= int(input())

# ter1= ["a" for x in range(cant_ter1)]

# for i in range(0,cant_ter1):
#     print("ingrese terminal ", (i + 1),": " )
#     a = input()
#     ter1[i] = a




 #estados automata 1

# print("estados del automata 1")

def est():
    
    print ("ingrese cantidad de estados del automata  :")
    cant_est_auto = int(input())

    estados= ["a" for x in range(cant_est_auto)]

    for i in range(0,cant_est_auto):
        print("ingrese estado ", (i + 1),": ")
        a = input()
        estados.append(a)

    return estados










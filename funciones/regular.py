#Grafo Regular
#Es aquel grafo cuyos vertices tienen todos el mismo grado



# def g_regular(x,n):
#     cant=0
#     iguales=0
#     for i in range(0,n):
#         gradov=0
#         for j in range(0,n):
#             if x[i][j]==1:
#                 gradov+=1
#         if i==0:
#             cant+=1
#             iguales=gradov
#         if iguales==gradov:
#             cant+=1
#         else:
#             return False
#     if cant==n:
#         return True
#     else:
#         return False
        





def g_regular(x,n):      
    arreglo_grados = [0 for x in range(n)]
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=x[i][j]
        arreglo_grados[i]=acum
    
    contador=0
    for i in range(0,n):
        if arreglo_grados[0]==arreglo_grados[i]:
            contador+=1
#    print("¿Es Regular?")
    if n == 0:
        return False  
    if contador==n:
        return True
    else:
        return False

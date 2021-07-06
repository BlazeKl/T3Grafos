# X es el arreglo bidimensional (matriz)
# n es el largo del arreglo, matriz n*n cuadrada

def is_euleriano(x,n):      
    arreglo_grados = [0 for x in range(n)]
    for i in range(0,n):
        acum=0
        for j in range(0,n):
            acum+=x[i][j]
        arreglo_grados[i]=acum

    contador=0
    for i in range(0,n):
        if arreglo_grados[i]%2== 0:
            contador+=1
    print("¿Es Euleriano?")
    if n == 0:
        return False  
    if contador==n:
        return True
    else:
        return False
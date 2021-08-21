# from .numregiones import cantidad_regiones
from .prim import prim_tp
# from .kruskal import kruskal_tp
from .kruskalXD import adyacencia_peso

class grafo:
    def __init__(self,N):
        self.N = N
        self.g_matr = [[0 for x in range(N)] for y in range(N)]
        self.g_peso = [[0 for x in range(N)] for y in range(N)]

    def set_n(self,x,i,j):
        self.g_matr[i][j] = x

    def set_p(self,x,i,j):
        self.g_peso[i][j] = x

    def get_n(self,i,j):
        return self.g_matr[i][j]

    def get_p(self,i,j):
        return self.g_peso[i][j]

    def print_mat(self,limit):
        for i in range (0,limit):
            for j in range (0,limit):
                print(" ",+self.g_matr[i][j], end = " "),
            print("\n")

    def print_pes(self,limit):
        for i in range (0,limit):
            for j in range (0,limit):
                print(" ",+self.g_peso[i][j], end = " "),
            print("\n")

    # def n_regiones(self,a,v):
    #     return cantidad_regiones(a,v)

    def l_kruskal(self,limit):
        return kruskal_tp(self.g_peso,limit)

    def l_prim(self,limit,init):
        return prim_tp(self.g_peso,limit,init)

    def l_kruskal2(self,limit):
        return adyacencia_peso(self.g_peso,limit)
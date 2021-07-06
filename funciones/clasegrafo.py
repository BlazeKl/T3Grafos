from .euleriano import is_euleriano
from .hamiltoniano import is_hamiltoniano
from .gradosaristas import gradosgrafo
from .numcromatico import num_cromatico
from .colorear import l_colorear
from .camino import matriz_c
from .conexo import is_conexo
from .rueda import g_rueda
from .completo import g_completo
from .simple import g_simple
from .regular import g_regular
from .numregiones import cantidad_regiones

class grafo:
    def __init__(self,N):
        self.N = N
        self.g_matr = [[0 for x in range(N)] for y in range(N)]
        self.g_peso = [[0 for x in range(N)] for y in range(N)]

    def set_n(self,x,i,j):
        self.g_matr[i][j] = x

    def sum_p(self,x,i,j):
        self.g_peso[i][j] += x

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

    def get_grado(self,limit):
        return gradosgrafo(self.g_matr,limit)

    def do_cromatico(self,limit):
        return num_cromatico(self.g_matr,limit)

    def do_colorear(self,limit):
        return l_colorear(self.g_matr,limit)

    def euleriano(self,limit):
        return is_euleriano(self.g_matr,limit)

    def get_camino(self,limit):
        return matriz_c(self.g_matr,limit)

    def conexo(self,limit):
        return is_conexo(self.g_matr,limit)

    def rueda(self,limit):
        return g_rueda(self.g_matr,limit)

    def completo(self,limit):
        return g_completo(self.g_matr,limit)

    def simple(self,limit):
        return g_simple(self.g_matr,limit)
    
    def regular(self,limit):
        return g_regular(self.g_matr,limit)

    def n_regiones(self,a,v):
        return cantidad_regiones(a,v)
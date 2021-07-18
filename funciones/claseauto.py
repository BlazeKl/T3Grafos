from .drawauto import draw

class automata:
    def __init__(self):
        self.estados = []
        self.transiciones = []
        self.inicial = []
        self.alfa = []
        self.final = []

    def set_estados(self,input):
        self.estados = input

    def set_tran(self,input):
        self.transiciones = input

    def set_inicial(self,input):
        self.inicial = input

    def set_alfa(self,input):       #almacena el alfabeto del automata. ej: transicion con [0,1] o [a,b,c] 
        self.alfa = input

    def set_final(self,input):
        self.final = input
        print(input)

    def bdraw(self):
        draw(self.alfa,self.estados,self.inicial,self.transiciones,self.final)
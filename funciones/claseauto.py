from .drawauto import draw

class automata:
    def __init__(self):
        self.estados = []
        self.transiciones = []
        self.inical = []
        self.alfa = []
        self.terminal = ()

    def set_estados(self,input):
        self.estados = input

    def app_estados(self,input):
        self.estados.append(input)

    def set_tran(self,input):
        self.transiciones = input

    def app_tran(self,input):
        self.transiciones.append(input)

    def set_inicial(self,input):
        self.inicial = input

    def set_alfa(self,input):       #almacena el alfabeto del automata. ej: transicion con [0,1] o [a,b,c] 
        self.alfa = input

    def set_final(self,input):
        self.terminal = input

    def app_final(self,input):
        self.terminal.append(input)

    def bdraw(self):
        draw(self.estados,self.transiciones,self.inical,self.alfa,self.terminal)
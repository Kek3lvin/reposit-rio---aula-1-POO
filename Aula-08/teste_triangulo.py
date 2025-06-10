class Triangulo():
    def __init__(self, base, altura):
        self.b = base
        self.h = altura
    def set_b(self,v):
        if v < 0: raise ValueError('O valor da base deve ser positivo!')
        self.b = v
    def set_h(self,v):
        if v < 0: raise ValueError('O valor da altura deve ser positivo!')
        self.h = v
    def get_b(self):
        return self.b
    def get_h(self):
        return self.h
    def calc_area(self):
        return self.get_b * self.get_h / 2 


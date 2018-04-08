class ClassExemplo
    ladoA = None
    ladoB = None



    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        print('Nova instancia')

    def calculaArea(self):
        return self.ladoA*self.ladoB
        

        
class ClasseExemploExtendida(ClassExemplo)

    def __init__(self):
        
        print('Nova instancia da classe extendida')

    def calculaPerimetro(self):
        return 2*self.ladoA+2*self.ladoB



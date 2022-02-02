class Automobile():
    def __init__(self, casa_autonomo, modello, numero_posti, targa):
        self.casa_autonomo= casa_autonomo
        self.modello= modello
        self.numero_posti= numero_posti
        self.targa= targa
    
    def __str__(self):
        return ('Casa automobilistica: {},Modello: {}, Numero posti: {}, Targa: {}'.format(self.casa_autonomo, self.modello, self.numero_posti, self.targa))
    
    def parla(self):
        print('Broom Broom PORCODIOOOOO')
    
    def confronto(self):
        if self.casa_autonomo1 != self.casa_autonomo2:
            print('Casa diversa')
        if self.modello1 != self.modello2:
            print('Modello diverso')
        if self.numero_posti1 != self.numero_posti2:
            print('Posti diversi')
class Transformer(Automobile):
    def __init__(self, nome, gen, grado, reparto)
car1= Automobile('Ferrari', 'F11', '2', 'suck')
print(car1)
car1.parla
car2=Automobile('Mazda', 'MPV', '7', 'cock')

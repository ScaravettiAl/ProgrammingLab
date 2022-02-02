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
    
    def confronto(self, casa_autonomo1, modello1, numero_posti1):
        self.casa_autonomo1=casa_autonomo1
        self.modello1=modello1
        self.numero_posti1=numero_posti1
        if self.casa_autonomo != self.casa_autonomo1:
            print('Casa diversa')
        if self.modello1 != self.modello:
            print('Modello diverso')
        if self.numero_posti1 != self.numero_posti:
            print('Posti diversi')

class Transformer(Automobile):
    def __init__(self, casa_autonomo, modello, numero_posti, targa, nome, gen, grado, reparto):
        super().__init__(casa_autonomo, modello, numero_posti, targa)
        self.nome=nome
        self.gen=gen
        self.grado=grado
        self.reparto= reparto
    def scheda_militare(self):
        print('Nome: {}, Generazione:{}, Grado:{}, Reparto:{}'.format(self.nome, self.gen, self.grado, self.reparto))


car1= Automobile('Ferrari', 'F11', '2', 'suck')
print(car1)
car1.parla()

car2=Automobile('Mazda', 'MPV', '7', 'cock')
car1.confronto(car2.casa_autonomo, car2.modello, car2.numero_posti)

print(type(car1))

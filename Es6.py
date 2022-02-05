class Calcolatrice():
    def __init__(self, a, b):
        self.a=a
        self.b=b
        try:
            int(self.a)
            int(self.b)
        except:
            raise Exception('Qualcosa non va')
    
    def somma(self):
        return self.a+self.b
    def differenza(self):
        return self.a-self.b
    def moltiplicazione(self):
        return self.a*self.b
    def divisione(self):
        if(self.b==0):
            raise Exception('Qualcosa non va')
        return self.a/self.b
    def potenza(self):
        if(isinstance(self.a, int) and isinstance(self.b, int)):
            return self.a**self.b
        else:
            raise Exception('Qualcosa non va')
    def modulo(self):
        return abs(self.a) and abs(self.b)
    def radice(self):
        if(self.a>0 and self.b>0):
            return self.a**(1/self.b)
        else:
            raise Exception('Qualcosa non va')
    
                
class Test():
    def test(self):
        test1= Calcolatrice(4, 2)
        test2= Calcolatrice(1.5, 2.5)
        test3= Calcolatrice('2', '4')
        if not test1.somma == 6:
            raise Exception('Test somma non passato')
        if not test2.somma == 4:
            raise Exception('Test somma non passato')
        if not test1.somma == 6:
            raise Exception('Test somma non passato')
        if not test1.differenza == 2:
            raise Exception('Test differenza non passato')
        if not test2.differenza == -1:
            raise Exception('Test differenza non passato')
        if not test1.differenza == -2:
            raise Exception('Test differenza non passato')


prova= Calcolatrice(5,7)
x=prova.somma()
print(x)
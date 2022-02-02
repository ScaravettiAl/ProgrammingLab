import random
class Automa():
    def __init__(self):
        self.biancheria=None
        self.calzini=None
        self.maglia=None
        self.pantaloni=None
        self.calzatura=None
    
    def bianch(self):
        self.biancheria=True
        return 1
    def calz(self):
        self.calzini=True
        return 1
    def magl(self):
        self.maglia=True
        return 1
    def pant(self):
        self.pantaloni=True
        return 1
    def calza(self):
        self.calzatura=True
        return 1

def esegui(automa, capo):
    if capo=='biancheria':
        if (random.randint(0,1))== 1:
            automa.bianch()
        else:
            return 0
    if capo=='maglia':
        if (random.randint(0,1))== 1:
            automa.magl()
        else:
            return 0
    if capo=='calzini':
        if (random.randint(0,1))== 1:
            automa.calz()
        else:
            return 0
    if capo=='pantaloni':
        if (random.randint(0,1))== 1:
            automa.pant()
        else:
            return 0
    if capo=='calzatura':
        if (random.randint(0,1))== 1:
            automa.calza()
        else:
            return 0

automa= Automa()
capi_vestiario=['biancheria', 'calzini', 'maglia', 'pantaloni', 'calzatura']
vestito= True
i=0
for i in range(0, 5):
    x=capi_vestiario[i]
    print(i)
    print(x)
    #x=random.choice(capi_vestiario)
    #if(x!=capi_vestiario[i]):
    #    raise Exception
    y=esegui(automa, x)
    if y==1:
        print('successo')
    elif y==0:
        print('fallimento')

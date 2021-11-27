def stampa(lista):
    for item in lista:
        print(item)

def stats(lista):
    lista3=[]
    r=True
    for item in lista:
        if  int(item) != item :
            r=False
            print('La lista non è una lista di interi')
    
    if r == True:
        #somma
        somma=sum(lista)
        print(somma)
        #media
        media=somma/len(lista)
        print(media)
        #minimo
        min=lista[0]
        for item in lista:
            if item < min :
                min=item
        print(min)
        #massimo
        max=lista[0]
        for item in lista:
            if max < item :
                max=item
        print(max)

def somma_vettoriale(lista1, lista2):
    r=True
    lista3=[]
    for item in lista1:
        if  int(item) != item :
            r=False

    for item in lista2:
        if  int(item) != item :
            r=False
    if(len(lista1)!=len(lista2)):
        r=False
    
    if(r==True):
        for i in range(len(lista1)):
            s=lista1[i]+lista2[i]
            lista3.append(s)
        return lista3
    if(r==False):
        return lista3


lista=[1,2,3,4.05,5]
stampa(lista)
stats(lista)
print(somma_vettoriale(lista, lista))
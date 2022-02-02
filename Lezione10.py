class CSVFile():
    def __init__(self, name):
        self.name = name
        

    def getdata(self):
        try:
            file=open(self.name, 'r')
            file.readline()
        except:
            print('ERRORE')

        data=[]
        file=open(self.name, 'r')
        for line in file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            
            if elements[0] != 'Date':
                data.append(elements)
        file.close()
        return data

class NumericalCSVFile(CSVFile):
    def getdata(self):
        string_data = super().getdata()
        numerical_data = []

        for string_row in string_data:
            numerical_row = []

            for i,element in enumerate(string_row):
                if i == 0:
                    numerical_row.append(element) 
                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data

class Model():
    def fit(self, data):
        raise NotImplementationError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementationError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        i=0
        n=0
        
        for item in data:
            if(i<len(data)-1):
                n += data[i+1]-data[i]
        
                i+=1
        return n/(len(data)-1)+data[-1]

class FitIncrementModel(IncrementModel):
    def fit(self, data):
        i=0
        n=0
        
        for item in data:
            if(i<len(data)-1):
                n += data[i+1]-data[i]
        
                i+=1
        self.avg_increment= n/(len(data)-1)

    def predict(self, data):
        parent_predict=super().predict(data)
        parent_predict_increment = parent_predict - data[-1]
        pred_increment=(self.avg_increment+parent_predict_increment)/2
        prev= data[-1]+pred_increment
        return prev

sales=[]
file_numerico=NumericalCSVFile('shampoo_sales.csv')
lista_num=file_numerico.getdata()
for i,element in lista_num:
    sales.append(element)
print(sales)

modello1=IncrementModel()
s1=0
e1=23
terr1=0
for i in range(24, 36):
    x1=modello1.predict(sales[s1:e1])
    print('Valutazione:{}'.format(x1))
    print('Valore effettivo: {}'.format(sales[i]))
    err=abs(x1-sales[i])
    print('Errore:{}'.format(err))
    print('------------------------')
    s1+=1
    e1+=1
    terr1+=err
print('Errore medio: {}'.format(terr1/12))

print('++++++++++++++++++++++++')

modello2=FitIncrementModel()
s=0
e=23
terr=0
for i in range(24, 36):
    modello2.fit(sales[s:e-3])
    x=modello2.predict(sales[e-3:e])
    print('Fit:{}'.format(x))
    print('Valore effettivo: {}'.format(sales[i]))
    err=abs(x-sales[i])
    print('Errore:{}'.format(err))
    print('------------------------')
    s+=1
    e+=1
    terr+=err

print('Errore medio: {}'.format(terr/12))

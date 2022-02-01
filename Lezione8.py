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
        n=0
        x=len(data)-1
        for i in range(1,3):
            n+=data[x]-data[x-1]

            x=x-1
        return (n/2)+data[len(data)-1]

class FitIncrementModel(IncrementModel):
    def fit(self, data):
        i=0
        n=0
        
        for item in data:
            if(i<len(data)-1):
                n += data[i+1]-data[i]
        
                i+=1
        return n  

    def predict(self, n, data):
        return n/(len(data)-1)+data[len(data)-1]
        

sales=[]
file_numerico=NumericalCSVFile('shampoo_sales.csv')
lista_num=file_numerico.getdata()
for i,element in lista_num:
    sales.append(element)
print(sales)

modello1=IncrementModel()
print(modello1.predict(sales))

modello2=FitIncrementModel()
n=modello2.fit(sales)
print(modello2.predict(n, sales))
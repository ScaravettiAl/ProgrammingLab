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
        l=[]
        for i in data:
            y=data[i]
            l.append(y[1])
            
        i=0
        x=0
        c=0
        for item in l:
            if(i!=0):
                x=x + l[i]-l[i-1]
                print(x)
                c+=1
            i+=1
        prevision= (x/c) + l[i-1]
       
        return prediction

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

file = CSVFile('shampoo_extract.csv')
print('Dati: "{}"'.format(file.getdata()))

file_numerico=NumericalCSVFile('shampoo_extract.csv')
print('Dati: "{}"'.format(file_numerico.getdata()))

#file1=CSVFile('test,csv')
#print('Dati: "{}"'.format(file1.getdata()))

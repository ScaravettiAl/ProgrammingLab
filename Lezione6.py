class CSVFile():
    def __init__(self, name):
        if(isinstance(name, str)==False):
            raise Exception('Errore')
        self.name = name

    def getdata(self, start=None, end=None):
        try:
            file=open(self.name, 'r')
            file.readline()
        except:
            print('ERRORE')

        if()
        data=[]
        file=open(self.name, 'r')
        for line in file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            
            if elements[0] != 'Date':
                data.append(elements)
        file.close()
        return data

      
file = CSVFile('shampoo_sales.csv')
print('Dati: "{}"'.format(file.getdata()))

file1= CSVFile(5)
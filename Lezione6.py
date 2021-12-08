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

        if(start!=None and end!=None):
            s=int(start)
            e=int(end)
            c=0
            data=[]
            file=open(self.name, 'r')

            for line in file:
                if(c in range(s, e)):
                    elements = line.split(',')
                    elements[-1] = elements[-1].strip()
                    
                    if elements[0] != 'Date':
                        data.append(elements)
                c=c+1
            file.close()
            return data

      
file = CSVFile('shampoo_sales.csv')
print('Dati: "{}"'.format(file.getdata(0, 5)))

#file1= CSVFile(5)
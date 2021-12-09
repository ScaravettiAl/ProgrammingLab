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
        else:
            data=[]
            file=open(self.name, 'r')
            for line in file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
            
                if elements[0] != 'Date':
                    data.append(elements)
        file.close()
        return data
      
file = CSVFile('shampoo_extract.csv')
file1= CSVFile('extract2.csv')
file2= CSVFile('shampoo_sales.csv')

if not (file.getdata() == file1.getdata()):
    raise Exception('Test non passato')
if not(file.getdata() == file2.getdata()):
    raise Exception('Test non passato')


class CSVFile():
    def __init__(self, name):
        self.name = name
        

    def getdata(self):
        try:
            file=open(self.name, 'r')
            file.readline()
        except Exception as e:
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
    
    def get_date_vendite(self):
        from datetime import datetime
        values=[]
        i=0
        file=open(self.name, 'r')
        for line in file:
                elem=line.split(',')  
                if elem[0] != 'Date':
                    value=elem[0]
                    mydate= datetime.strptime (elem[0], '%d-%m-%Y')
                    values.append(mydate)
        for data in values:
            print(data.strftime('%d-%m-%Y'))
        file.close()
    
    def __str__(self):
        file=open(self.name, 'r')
        for line in file:
            elem=line.split(',')
            if elem[0]== 'Date':
                return line

file= CSVFile('shampoo_extract.csv')
file.get_date_vendite()
print(file)

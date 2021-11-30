class CSVFile():
    def __init__(self, name):
        if(isinstance(name, str)==False):
            raise Exception('Errore')
        self.name = name

    def getdata(self, start= None, end= None):
        #if(start == NONE && )
        int(start)
        int(end)
        a_list=[]
        f_list=[]
        file=open(self.name, 'r')
        
        for line in file :
            for line in range(start, end):
                elements = line.split(',')
                
                if elements[0] != 'Date':
                    date = elements[0]
                    value = elements[1]
                    a_list.append(date) 
                    a_list.append(value)
                    f_list.append(a_list)
            
        return f_list

      
v = CSVFile('shampoo_sales.csv')
#v0= CSVFile(5)


v2=v.getdata(0, 10)
print(v2)
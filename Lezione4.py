class CSVFile():
    def __init__(self, name):
        self.name = name

    def getdata(self):
        a_list=[]
        f_list=[]
        #i=0
        file=open(self.name, 'r')
        for line in file:
            #if(i<3):
                elements = line.split(',')
                
                if elements[0] != 'Date':
                    date = elements[0]
                    value = elements[1]
                    a_list.append(date) 
                    a_list.append(value)
                    f_list.append(a_list)
                    a_list=[]
            #i+=1
        
        return f_list

v = CSVFile('shampoo_sales.csv')


print(v.getdata())
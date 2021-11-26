class CSVFile():
    def __init__(self, name):
        self.name = name

    def getdata(self):
        a_list=[]
        f_list=[]
        file=open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1]
                a_list.append(date, value)
                f_list.append(a_list)
        
        return f_list

v = CSVFile('shampoo_sales')

v2=v.getdata()
print(v2)
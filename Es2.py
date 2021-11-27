def fun_data():
    values=[]
    i=0
    file=open('shampoo_sales.txt', 'r')
    for line in file:
        if(i<3):
            elem=line.split(',')  
            if elem[0] != 'Date':
                value=elem[0]
                values.append(value)
                i=i+1
    return values
    file.close()

print(fun_data())

values=[]
i=0

file=open('shampoo_sales.txt', 'r')
for line in file:
    if(i<3):
        elem=line.split(',')  
        if elem[0] != 'Date':
            value=elem[1]
            values.append(float(value))
            i=i+1
print (sum(values))
file.close()
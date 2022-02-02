def fun_data():
    from datetime import datetime
    values=[]
    i=0
    file=open('shampoo_sales.txt', 'r')
    for line in file:
        if(i<3):
            elem=line.split(',')  
            if elem[0] != 'Date':
                value=elem[0]
                mydate= datetime.strptime (elem[0], '%d-%m-%Y')
                values.append(mydate)
                i=i+1
    for data in values:
        print(data.strftime('%d-%m-%Y'))
    file.close()

fun_data()
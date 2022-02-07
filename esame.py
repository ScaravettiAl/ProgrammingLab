class ExamException(Exception):
    pass
    
class CSVFile:

    def __init__(self, name):
        self.name = name

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except:
            self.can_read = False
        

    def get_data(self):
        
        if not self.can_read:
            raise ExamException('Errore, file inesistente')

        else:
            data = []
            my_file = open(self.name, 'r')

            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()

                if elements[0] != 'date':
                    data.append(elements)
            
            my_file.close()
            return data

class CSVTimeSeriesFile(CSVFile):
    
    def get_data(self):
        string_data = super().get_data()
        numerical_data = []
        check_data=[]
        cfr_year=0
        cfr_month=0

        for string_row in string_data:
            numerical_row = []

            for i,element in enumerate(string_row):
                print(enumerate(string_row))
                if i == 0:
                    numerical_row.append(element)
                    y_e_m=element.split('-')
                    year=int(y_e_m[0])
                    month=int(y_e_m[1])
                    if cfr_year>year:
                        raise ExamException('Errore, date fuori ordine')
                    if cfr_year==year and cfr_month>=month:
                        raise ExamException('Errore, date fuori ordine')
                    cfr_year=year
                    cfr_month=month
                    if check_data==element:
                        raise ExamException('Errore, duplicato trovato')
                    check_data=element
                else:
                    print(element)
                    try:
                        if int(element)>0:
                            numerical_row.append(int(element))
                    except:
                         pass
                    """
                    try:
                        print(element)
                        dati=element.split(',')
                        print(dati[0])
                        try:
                            if int(dati[0])>0:
                                numerical_row.append(int(dati[0]))
                        except:
                            pass
                    except:
                        try:
                            if int(element)>0:
                                numerical_row.append(int(element))
                        except:
                            pass"""

            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data

def compute_avg_monthly_difference(time_series, first_year, last_year):
    if not type(first_year) is str:
        raise ExamException('Errore, anno in input non di tipo str')
    if not type(last_year) is str:
        raise ExamException('Errore, anno in input non di tipo str')
    new_time_series=[]
    for string_row in time_series:
        new_data=[]
        for i,element in enumerate(string_row):
            if i==0:
                dat=element.split('-')
                new_data.append(int(dat[0]))
                new_data.append(int(dat[1]))
            else:
                new_data.append(element)
        new_time_series.append(new_data)

    tmp=[]
    y=0
    avg=[]
    check=False
    for i in range(1, 13):
        for string_row in new_time_series:
            if string_row[0] in range(int(first_year), int(last_year)+1):
                if string_row[1]==i:
                    tmp.append(string_row[2])
                check= True
        if check == False:
            raise ExamException('Errore, anno non trovato')

        if len(tmp)-1==0:
            avg.append(0)
        else:
            for i in range(0, len(tmp)-1):
                y=y+tmp[i+1]-tmp[i]
            avg.append(y/(len(tmp)-1))
        y=0
        tmp=[]    
    return avg
            
#test=CSVFile(name='data.csv')
#print(test.get_data())
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series= time_series_file.get_data()
print(time_series)
print('----------------------')
print(compute_avg_monthly_difference(time_series, '1949', '1950'))
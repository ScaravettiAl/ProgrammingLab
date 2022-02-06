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

        for string_row in string_data:
            numerical_row = []

            for i,element in enumerate(string_row):
                
                if i == 0:
                    numerical_row.append(element)
                    
                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data

def compute_avg_monthly_difference(time_series, first_year, last_year):
    """
    try:
        first_year=int(first_year)
        last_year=int(last_year)
    except:
        raise ExamException('Errore, input non validi')
    """
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

        for i in range(0, len(tmp)-1):
            y=y+tmp[i+1]-tmp[i]
        avg.append(y/(len(tmp)-1))
        y=0
        tmp=[]    
    return avg
            

time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series= time_series_file.get_data()
print(time_series)
print('----------------------')
print(compute_avg_monthly_difference(time_series, '1949', '1951'))
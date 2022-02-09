from datetime import datetime

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
        i=0
        tmp=[]

        if not self.can_read:
            raise ExamException('Errore, file inesistente')             
        else:
            data = []
            my_file = open(self.name, 'r')

            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()

                if elements[0] != 'date':
                    if len(elements)<2:         
                        pass
                    else:
                        for i in range(0,2):            
                            tmp.append(elements[i])
                        
                        data.append(tmp)
                        tmp=[]
            my_file.close()
            return data

class CSVTimeSeriesFile(CSVFile):
    
    def get_data(self):
        
        string_data = super().get_data()        
        
        numerical_values = []                     
        check_data=[]                           
        cfr_year=0                              
        cfr_month=0                             

        for string_row in string_data:
            numerical_row = []                  

            for i,element in enumerate(string_row):                     
                if i == 0 and '-' in element:                           
                    numerical_row.append(element)
                    y_e_m=datetime.strptime(element, '%Y-%m')            
                    year=y_e_m.year
                    month=y_e_m.month
                    
                    if cfr_year>year:                                           
                        raise ExamException('Errore, date fuori ordine')
                    if cfr_year==year and cfr_month>month:
                        raise ExamException('Errore, date fuori ordine')
                    cfr_year=year
                    cfr_month=month
                    if check_data==element:
                        raise ExamException('Errore, duplicato trovato')
                    check_data=element
                else:
                    try:
                        if int(element)>0:                      
                            numerical_row.append(int(element))
                    except:                                         
                        pass

            if len(numerical_row) == len(string_row):                   
                numerical_values.append(numerical_row)
        return numerical_values

def compute_avg_monthly_difference(time_series, first_year, last_year):
    
    if not type(first_year) is str:                                            
        raise ExamException('Errore, anno in input non di tipo str')
    if not type(last_year) is str:
        raise ExamException('Errore, anno in input non di tipo str')
    
    new_time_series=[]
    for string_row in time_series:                              
        numerical_data=[]                                      
        for i,element in enumerate(string_row):
            if i==0:
                date=datetime.strptime(element, '%Y-%m')
                numerical_data.append(date.year)
                numerical_data.append(date.month)
            else:
                numerical_data.append(element)
        new_time_series.append(numerical_data)

    month_values=[]                  
    y=0
    avg=[]                          
    check=False
    for i in range(1, 13):                                  
        for string_row in new_time_series:
            if string_row[0] in range(int(first_year), int(last_year)+1):       
                if string_row[1]==i:
                    month_values.append(string_row[2])                  
                check= True

        if check == False:                                          
            raise ExamException('Errore, anno non trovato')

        if len(month_values)==1:                         
            avg.append(0)
        else:
            for i in range(0, len(month_values)-1):          
                y=y+month_values[i+1]-month_values[i]
            avg.append(y/(len(month_values)-1))
        y=0
        month_values=[]    
    return avg

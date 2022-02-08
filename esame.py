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
                    if len(elements)<2:         #se le righe son vuote o contengono cose a caso o non c'è la rilevazione per un mese 
                        pass
                    else:
                        for i in range(0,2):            #se c'è un campo in più lo ignoro
                            tmp.append(elements[i])
                        data.append(tmp)
                        tmp=[]
            my_file.close()
            return data

class CSVTimeSeriesFile(CSVFile):
    
    def get_data(self):
        string_data = super().get_data()        #richiamo il modulo della funzione madre
        numerical_data = []                     #lista di liste che hanno l'anno in formato stringa e i rilevamenti come interi 
        check_data=[]                           #lista che mi permette di confrontare le date che leggo
        cfr_year=0                              #variabile che mi permette di confrontare gli anni
        cfr_month=0                             #variabile che mi permette di confrontare i mesi

        for string_row in string_data:
            numerical_row = []                  

            for i,element in enumerate(string_row):
                #if i==0 and not '-' in element:
                #    pass
                if i==0 and '-' in element:
                    numerical_row.append(element)
                    y_e_m=element.split('-')            #divido la data e faccio i controlli per date fuori posto o duplicati
                    year=int(y_e_m[0])
                    month=int(y_e_m[1])
                    
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
                        if int(element)>0:                      #verifico che il rilevamento sia di tipo intero positivo
                            numerical_row.append(int(element))
                    except:
                        pass

            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data

def compute_avg_monthly_difference(time_series, first_year, last_year):
    if not type(first_year) is str:                                               #verifico che gli anni in input siano stringhe
        raise ExamException('Errore, anno in input non di tipo str')
    if not type(last_year) is str:
        raise ExamException('Errore, anno in input non di tipo str')
    if int(first_year)>int(last_year):
        raise ExamException('Errore, inserimento anni')
    new_time_series=[]
    for string_row in time_series:                        #trasformo la data in valori interi
        new_data=[]
        for i,element in enumerate(string_row):
            if i==0:
                dat=element.split('-')
                new_data.append(int(dat[0]))
                new_data.append(int(dat[1]))
            else:
                new_data.append(element)
        new_time_series.append(new_data)

    tmp=[]                  #lista che conterrà i rilevamenti del mese
    y=0
    avg=[]
    check=False
    for i in range(1, 13):
        for string_row in new_time_series:
            if string_row[0] in range(int(first_year), int(last_year)+1):       #cerco l'anno 
                if string_row[1]==i:
                    tmp.append(string_row[2])
                check= True

        if check == False:                                          #se check=False allora non ho trovato l'anno
            raise ExamException('Errore, anno non trovato')

        if len(tmp)==1:                         #se la lista contiene solo un rilevamento per quel mese la media varrà 0
            avg.append(0)
        else:
            for i in range(0, len(tmp)-1):          #faccio i calcoli e inserisco nella lista
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
print(compute_avg_monthly_difference(time_series, '1949', '1951'))
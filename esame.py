from datetime import datetime

class ExamException(Exception):
    pass
    
class CSVFile:                      #classe vista a lezione

    def __init__(self, name):
        self.name = name

        self.can_read = True
        try:
            my_file = open(self.name, 'r')              #verifica esistenza file
            my_file.readline()
        except:
            self.can_read = False
        

    def get_data(self):
        i=0
        tmp=[]                              #lista temporanea in cui poi inserisco solo data e valori
        if not self.can_read:
            raise ExamException('Errore, file inesistente')             #verifica esistenza file

        else:
            data = []
            my_file = open(self.name, 'r')

            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()

                if elements[0] != 'date':
                    if len(elements)<2:         #se le righe son vuote o contengono cose a caso o non c'è la rilevazione per un mese salto la riga
                        pass
                    else:
                        for i in range(0,2):            #se c'è un campo in più lo ignoro, inserisco solo i primi due valori, cioè data e rilevamento
                            tmp.append(elements[i])
                        data.append(tmp)
                        tmp=[]
            my_file.close()
            return data

class CSVTimeSeriesFile(CSVFile):
    
    def get_data(self):
        string_data = super().get_data()        #richiamo il modulo della classe madre
        numerical_values = []                     #lista di liste che hanno l'anno in formato stringa e i rilevamenti come interi 
        check_data=[]                           #lista che mi permette di confrontare le date che leggo
        cfr_year=0                              #variabile che mi permette di confrontare gli anni
        cfr_month=0                             #variabile che mi permette di confrontare i mesi

        for string_row in string_data:
            numerical_row = []                  

            for i,element in enumerate(string_row):                     #divido e numero gli elementi di ogni lista 
                if i == 0 and '-' in element:                           #vedo se il primo elemento è una data nella forma anno-mese
                    numerical_row.append(element)
                    y_e_m=datetime.strptime(element, '%Y-%m')            #divido la data e faccio i controlli per date fuori posto o duplicati
                    year=y_e_m.year
                    month=y_e_m.month
                    
                    if cfr_year>year:                                           #confronti
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
                    except:                                         #altrimenti salto
                        pass

            if len(numerical_row) == len(string_row):                   #Alla fine aggiungo la riga in formato numerico alla lista "esterna", ma solo se sono riuscito a processare tutti gli elementi.
                numerical_values.append(numerical_row)
        return numerical_values

def compute_avg_monthly_difference(time_series, first_year, last_year):
    if not type(first_year) is str:                                               #verifico che gli anni in input siano stringhe
        raise ExamException('Errore, anno in input non di tipo str')
    if not type(last_year) is str:
        raise ExamException('Errore, anno in input non di tipo str')
    new_time_series=[]
    for string_row in time_series:                              #trasformo la data in valori interi
        numerical_data=[]                                      #lista con le date in formato intero
        for i,element in enumerate(string_row):
            if i==0:
                date=datetime.strptime(element, '%Y-%m')
                numerical_data.append(date.year)
                numerical_data.append(date.month)
            else:
                numerical_data.append(element)
        new_time_series.append(numerical_data)

    month_values=[]                  #lista che conterrà i rilevamenti del mese
    y=0
    avg=[]                          #lista finale
    check=False
    for i in range(1, 13):                                  #ciclo per tutti i mesi
        for string_row in new_time_series:
            if string_row[0] in range(int(first_year), int(last_year)+1):       #cerco l'anno 
                if string_row[1]==i:
                    month_values.append(string_row[2])                  #aggiungo il rilevamento
                check= True

        if check == False:                                          #se check=False allora non ho trovato l'anno
            raise ExamException('Errore, anno non trovato')

        if len(month_values)==1:                         #se la lista contiene solo un rilevamento per quel mese la media varrà 0
            avg.append(0)
        else:
            for i in range(0, len(month_values)-1):          #faccio i calcoli e inserisco nella lista
                y=y+month_values[i+1]-month_values[i]
            avg.append(y/(len(month_values)-1))
        y=0
        month_values=[]    
    return avg
            
#test=CSVFile(name='data.csv')
#print(test.get_data())
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series= time_series_file.get_data()
#print(time_series)
#print('----------------------')
print(compute_avg_monthly_difference(time_series, '1949', '1951'))
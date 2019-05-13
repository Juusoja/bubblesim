import csv
#import plotly.plotly as py


class CsvProcess:
# write into CSV

    # '13,1.80'
    
    #def __init__(self):
        
    def csvWrite(self,data,filename):
        with open(filename, 'w', newline = '') as f:

            writer = csv.writer(f, dialect = 'excel')
            for row in data:
                writer.writerow(row)

'''
    def csvRead(self,filename):
        #read
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                print(f'\t at time {row[0]}, the price is {row[1]}.'  )
'''
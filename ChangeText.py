# - *- coding: utf- 8 - *-
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    with open('resultTextForNum.csv', 'w') as file:
        for row in readCSV:
            writer = csv.writer(file)
            for i, line in enumerate(row):
                if(line == "MUITO BOM(A) (AS)"):
                    row[i] = 5
                elif(line == "BOM (A) (AS)"):
                    row[i] = 4
                elif(line == "REGULAR"):
                    row[i] = 3
                elif(line == "RUIM"):
                    row[i] = 2
                elif(line == "NÃO SE APLICA"):
                    row[i] = 1

            writer.writerow(row)
                
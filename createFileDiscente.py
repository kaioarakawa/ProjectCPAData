# - *- coding: utf- 8 - *-
import csv
from collections import defaultdict
from glob import iglob
questao = 1
eixo = 0
dimensao = 0
unique_headers = []
tipo = "CURSO"

columns = defaultdict(list) # each value in each column is appended to a list

for filename in iglob('*.csv'):
    with open("resultTextForNum.csv", 'rb') as fin:
        csvin = csv.reader(fin)
        unique_headers.append(next(csvin, []))
for a in unique_headers:
    title = a


with open("resultTextForNum.csv", 'rb')  as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)

with open('resultado.csv', 'w') as file: 
    writer = csv.writer(file)
    for x in range (1,161):
        if(x%2==1):
            if(1<=questao<=3):
               eixo = 1
               dimensao = 8
            elif(4<=questao<=5):
               eixo = 1
               dimensao = 1 
            elif(6<=questao<=10):
               eixo = 2
               dimensao = 3 
            elif(11<=questao<=20):
               eixo = 3
               dimensao = 2 
            elif(21<=questao<=27):
               eixo = 3
               dimensao = 9
            elif(28<=questao<=31):
               eixo = 3
               dimensao = 4
            elif(32<=questao<=50):
               eixo = 4
               dimensao = 6 
            elif(51<=questao<=52):
               eixo = 4
               dimensao = 10 
            elif(53<=questao<=66):
               eixo = 5
               dimensao = 7 
            questao = questao+1 
            for i, nota in enumerate(columns[x]): 
                text = [eixo]+[dimensao]+[title[x]]+[tipo]+[nota]+[columns[x+1][i]]
                writer.writerow(text)
         
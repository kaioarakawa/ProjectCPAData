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
               eixo = 3
               dimensao = 3 
            elif(11<=questao<=22):
               eixo = 3
               dimensao = 2 
            elif(23<=questao<=25):
               eixo = 3
               dimensao = 9
            elif(26<=questao<=29):
               eixo = 3
               dimensao = 4
            elif(30<=questao<=40):
               eixo = 4
               dimensao = 5 
            elif(41<=questao<=62):
               eixo = 4
               dimensao = 6 
            elif(63<=questao<=65):
               eixo = 4
               dimensao = 10
            elif(66<=questao<=80):
               eixo = 5
               dimensao = 7
            questao = questao+1 
            for i, nota in enumerate(columns[x]): 
                text = [eixo]+[dimensao]+[title[x]]+[tipo]+[nota]+[columns[x+1][i]]
                writer.writerow(text)
         
#! python3
# cp_data.py - copies specific data from csv

import csv, os
infile=open('exampleWithHeader.csv')
exre = csv.DictReader(infile)

output=open('output.csv','w')
outwi=csv.DictWriter(output,['name','qtde > 50'])
outwi.writeheader()

for row in exre:
    if (int(row['Quantity']) > 50):
        outwi.writerow({'name': row['Fruit'],'qtde > 50': row['Quantity']})

output.close()

import csv

file = open('data.csv','w')

datawrite=csv.writer(file)


body = [
    ['name','roll'],
    ['abhinav','0503'],
    ['bhanu teja','051A']
]

datawrite.writerows(body)

file.close()
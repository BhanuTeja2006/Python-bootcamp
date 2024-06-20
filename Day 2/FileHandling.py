#Reading data from file line by line using for each loop
file = open('example.txt','r')
i = 1
for data in file :
    print(i,') :',data)
    i+=1
file.close()
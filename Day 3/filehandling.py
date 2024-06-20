#Appending content and saving
file = open('example.txt','r')
content = file.readlines()
content.append('\nIm fine,how are you ?')
file.close()

#write data into file
writter = open('example.txt','w')
writter.writelines(content)
writter.close()
#reading data from file
reader = open('example.txt','r')
print(reader.read())
reader.close()
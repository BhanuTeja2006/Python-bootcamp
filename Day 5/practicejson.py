import json

file = open('data.json','w')

data = {
    "name" : "Abhinav",
    "age" : 19,
    "year" : 1
}

json.dump(data,file,indent=4)

file.close()
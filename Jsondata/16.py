import json
#dictionary
data={
    'name':'Sita',
    'age':20,
    'address':'ktm'
    
}
print(data)
#convert dictonary to json
jsondata=json.dumps(data)
print(jsondata)
#json to dictionary
data=json.loads(jsondata)
print(jsondata)

# print(dir(json))
# convert json data to file
# with open('jsondata/data.json','w') as file:
#     json.dump(data,file)
# read json data from file
with open('jsondata/data.json','r') as file:
    savedata=json.load(file)
    print(savedata)
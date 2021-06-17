import json

fObj = open('data.json', 'r')

data = json.load(fObj)['articles']


# for i in data['articles']:
# 	print(i)

print(data)

fObj.close()
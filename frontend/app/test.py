import json

f = open('1623926059.161785posts.json', 'r')

articles = json.load(f)


print(articles)

f.close()
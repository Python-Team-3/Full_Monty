import json
from urllib.request import urlopen

with urlopen('https://www.kulinarno-joana.com/') as response:
    source = response.read()

data = json.loads(source)
print(json.dumps(data, indent=2))
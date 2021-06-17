import json
import requests

class Post():
    
    def __init__(self, title, date, text) -> None:
        self.title = title
        self.date = date
        self.text = text
    
    def print_to_file(self, filename) -> None:
        with open(filename, 'a+') as f:
            # converts a Python object into a json strin
            jsonTitle = json.dumps(self.title)
            jsonDate = json.dumps(self.title)
            jsonText = json.dumps(self.title)

            # save the json data to a json file
            json.loads(jsonTitle)
            json.loads(jsonDate)
            json.loads(jsonText)
            json.loads((20 * '-') + '\n')
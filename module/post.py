import json
from json import encoder
import requests

class Post():
    
    def __init__(self, title, date, text, comments, common) -> None:
        self.title = title
        self.date = date
        self.text = text
        self.comments = comments
        self.common = common

    
    def print_to_file(self, filename) -> None:
        data = {}
        data['post'] = []
        data['post'].append({
            'title' : self.title,
            'date' : self.date,
            'text' : self.text,
            'common words' : self.common,
            'comments' : self.comments
            
        })

        with open(filename, 'a+', encoding= 'utf8') as f:

            # save the json data to a json file
            json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))


    def print_self(self):
        print(self.title)
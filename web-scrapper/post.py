#-*- coding: utf-8 -*-

import json

class Post():
    
    def __init__(self, title, date, text) -> None:
        self.title = title
        self.date = date
        self.text = text
    
    def print_to_file(self, filename) -> None:
        with open(filename, 'a+') as f:
            jsonTitle = json.dumps(self.title)
            jsonDate = json.dumps(self.title)
            jsonText = json.dumps(self.title)

            json.write(jsonTitle)
            json.write(jsonDate)
            json.write(jsonText)
            json.write((20 * '-') + '\n')

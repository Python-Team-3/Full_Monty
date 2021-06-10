class Post():
    
    def __init__(self, title, date, text) -> None:
        self.title = title
        self.date = date
        self.text = text
    
    def print_to_file(self, filename) -> None:
        with open(filename, 'a+') as f:
            f.write(self.title + '\n')
            f.write(self.date + '\n')
            f.write(self.text + '\n')
            f.write((20 * '-') + '\n')
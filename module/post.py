import json
from collections import Counter

class Post():
    
    WORD_LIST_LEN = 3
    MIN_WORD_LEN = 3
    PARAGRAPHS_LEN = 3

    def __init__(self, title, date, text, comments=None, first_paragraphs=None) -> None:
        self.title = title
        self.date = date
        self.text : str = text
        self.comments = comments
        self.paragraphs = first_paragraphs[0:Post.PARAGRAPHS_LEN]
    
    def _get_most_common_words(self, word_list):
        dict_to_return = {}
        words_to_count = (word for word in word_list if len(word) > Post.MIN_WORD_LEN)
        word_counter = Counter(words_to_count)
        words = word_counter.most_common(Post.WORD_LIST_LEN)
        
        for word in words:
            dict_to_return[word[0]] = word[1]

        return dict_to_return

    def get_as_json_object(self):
        return {"title_1" : self.title,
                           "date_of_publishing": self.date, 
                           "content":self.paragraphs, 
                           "most_used_words" : self._get_most_common_words(self.text.split(" ")),
                           "comments":self.comments}

    def print_to_text_file(self, filename) -> None:
        with open(filename, 'a+') as f:
            f.write(self.title + '\n')
            f.write(self.date + '\n')
            f.write(self.text + '\n')
            f.write((20 * '-') + '\n')
    
    @staticmethod
    def print_to_json_file(posts_list, filename):
        if not filename.endswith(".json"):
            filename += ".json"
        
        with open(filename, 'w', encoding= 'utf8') as file:
            file.write(json.dumps(posts_list, indent=4, ensure_ascii=False))
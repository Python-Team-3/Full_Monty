import pandas as pd
import json

df.columns = ['title_1', 'date_of_publishing', 'content', 'most_used_words', 'comments']
df.to_json('example.json')
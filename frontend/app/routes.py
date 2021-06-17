from app import app
from flask import render_template
import json

@app.route('/')
@app.route('/index')

def index():
#    return "I did not hit her, it's not true, it's bullshit, I did not... Oh, hi Mark!"

    user = {'username': 'Pesho'}

    f = open('app/data.json', 'r')

    articles = json.load(f)['articles']

    f.close()
 
    return render_template('index.html', title='Home', user=user, articles=articles)


@app.route('/post')

def post():

    return render_template('post.html', title='Home', user=user, articles=articles)
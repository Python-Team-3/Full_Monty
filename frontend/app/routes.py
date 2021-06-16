from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
#    return "I did not hit her, it's not true, it's bullshit, I did not... Oh, hi Mark!"

    user = {'username': 'Pesho'}
    posts = [
            {
                'author': {'username': 'Georgi'},
                'body': 'Just testing here!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The second test is way more beautiful!!'
            }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
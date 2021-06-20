from app import app
from flask import render_template
import json
from werkzeug.exceptions import abort

@app.route('/')
@app.route('/index')

def index():
    """
    index [summary]

    function for generating the index page

    Returns:
        [type]: [description]
    """

    user = {'username': 'Ангел'}

    f = open('app/the_data.json', 'r')

    articles = json.load(f)

    data = open('app/img_url.json', 'r')

    f.close()

    imgs = json.load(data)['articles']

    data.close()

    return render_template('index.html', title='Home', user=user, articles=articles, imgs=imgs)


def get_post(post_id):

    """
     [summary]

    Returns:
        [type]: [description]
    """

    f = open('app/the_data.json', 'r')

    articles = json.load(f)

    f.close()

    post = articles[post_id]

    if post_id > 19:
        abort(404)

    return post

@app.route('/<int:post_id>')
def post(post_id):

    """
     [summary]

    Returns:
        [type]: [description]
    """

    post = get_post(post_id)

    return render_template('post.html', title='Recipe post', post=post)


@app.route('/about')
def about_us():

    """
     [summary]

    Returns:
        [type]: [description]
    """

    us = ['Сияна', 'Калина', 'Димитър', 'Венци']

    return render_template('about-us.html', title='About', us=us)
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Roberto'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avangers movie was so cool'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'Naples is so beautiful, fantastic and amazon'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

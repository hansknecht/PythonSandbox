"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Markup
from BagOfSocks import app
from Reddit import Reddit

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message="A test of reading Reddit",
        redditList=Markup(get_top_submissions())
    )

def get_top_submissions():
    titles = "<ul>"
    reddit = Reddit()
    reddit.open_reddit_read()
    submissions = reddit.top_submissions('u_hansknecht', 5)
    for entry in submissions:
        titles += "<li>{0}</li>".format(entry.title)
    titles += "</ul>"
    return titles
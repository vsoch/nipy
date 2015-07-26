from flask import render_template
from app import app, pages
from functions import *
import os
# functions are imported in main.py to avoid circular imports

# Index Page
@app.route('/')
def home():

    projects,n,m = get_data()
    return render_template('index.html',projects=projects, n=n, m=m)

# Blog Roll
@app.route('/blog')
def blog():

    projects,n,m = get_data()
    posts = [page for page in pages if 'date' in page.meta]

    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('blog.html', pages=sorted_posts, projects=projects, n=n, m=m)

# Single blog page
@app.route('/<path:path>/')
def page(path):

    projects,n,m = get_data()

    # Path is the filename of a page, without the file extension
    # e.g. "welcome.md" --> "welcome"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page, projects=projects, n=n, m=m)

# Project page
@app.route('/project/<name>/')
def project(name):

    projects,n,m = get_data()

    # If the template file exists
    if os.path.exists("templates/%s.html" %(name)):
        page = "%s.html" %(name)
    else:
        page = "project.html"
    return render_template(page, projects=projects)

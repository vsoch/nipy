from flask import render_template
from app import app, pages
from functions import *
import os
# functions are imported in main.py to avoid circular imports

# Index Page
@app.route('/')
def home():

    pages = get_pages()
    projects,n,m = get_data()
    return render_template('index.html',projects=projects, n=n, m=m, page=pages[0])

# Blog Roll
@app.route('/blog/')
def blog():

    projects,n,m = get_data()
    pages = get_pages()

    return render_template('blog.html', pages=pages, projects=projects, n=n, m=m)

# Single blog page
@app.route('/pages/<path>/')
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
    df = get_project_df()
    project = df[df.markdown_tag == name]

    # If the template file exists
    if os.path.exists("templates/%s.html" %(name)):
        page = "%s.html" %(name)
    else:
        page = "project.html"
    return render_template(page, projects=projects, n=n, m=m, 
                           project=project["name"].tolist()[0], 
                           classname=project["class"].tolist()[0],
                           url=project["url"].tolist()[0],
                           github=project["github"].tolist()[0])


@app.route('/help/')
def help():
    projects,n,m = get_data()
    return render_template('help.html', projects=projects, n=n, m=m)

@app.route('/conduct/')
def conduct():
    projects,n,m = get_data()
    return render_template('conduct.html', projects=projects, n=n, m=m)

@app.route('/contribute/')
def contribute():
    projects,n,m = get_data()
    return render_template('contribute.html', projects=projects, n=n, m=m)



from flask import render_template
from app import app, pages
# functions are imported in main.py to avoid circular imports

# Index Page
@app.route('/')
def home():
    return render_template('index.html')

# Blog Roll
@app.route('/blog')
def blog():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('blog.html', pages=sorted_posts)

# Single blog page
@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "welcome.md" --> "welcome"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

# Project page
@app.route('/project/<name>/')
def project(name):

    # Get all projects
    projects = get_projects()

    # If the template file exists
    if os.path.exists("templates/%s.html" %(name)):
        page = "%s.html" %(name)
    else:
        page = "project.html"
    return render_template(page)

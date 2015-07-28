# Redesign for Nipy

[demo](http://www.vbmis.com/bmi/project/nipy)

#### How does this site work?
This is a flask site, meaning that the "back end" is in Python. We "freeze" it to generate a static version that can be served on nipy.github.io. Flask was chosen as an ideal solution as nipy is comprised of tools in python, and this means that examples, usage, etc., for each application can be integrated into a page.

#### What does it include?

##### Blog
Pages are automatically rendered from the "pages" folder into the blog portion of the site. To write an entry, simply make a new markdown file, and re-freeze the site (need instructions to do this - is it automatic?)

##### Projects
Projects, such as nibabel or nilearn, are arguably the most important content of this site. They are rendered in the navigation, the d3 visualization on the home page, and additionally, each has its own page. 

##### Iteractive visualization
The home page has a simple D3 visualization to show the different projects. This is ideal over a standard "corporate" image slider because it shows and gives immediate access to the content. This D3 is also produced dynamically (see below).

###### Adding a Project
Simply add the project name, a descriptor tag (used to name the page, and other programmatic stuffs), the url to its base, and its category in the [code/static/projects.tsv](code/static/projects.tsv) file. This will add the project to the site. 

###### Advanced / Custom Pages

- Option 1: If you want to add more information about the project (a custom page), then you simply need to add a template with the tag name (eg, "nilearn.html") to the code/templates folder. The app knows to look for this file, and if it exists, will render it over the default. This solution assumes you just want content that can be rendered with html/css.

- Option 2: If you desire to do more advanced stuffs (for example, rendering output produced by something in python) then you should write a custom view for the page in the code/views.py file. This is pretty easy to do - see the file itself for some examples, and ask for help if you need it.

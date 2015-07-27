from app import app, pages
import pandas

# Get main data for d3
def get_data():
    projects = get_projects()
    n = len(projects)
    m = get_count()
    return projects,n,m
 

def get_project_df():
    projects = pandas.read_csv("static/projects.tsv",sep="\t")
    return projects.sort(columns=["class","name"])
   
# Read in projects from tsv
def get_projects():
    projects = get_project_df()
    # Organize by class
    project_zip = []
    count=1
    for project_class in projects["class"].unique():
        project_subset = projects[projects["class"] == project_class]
        project_subset = zip(project_subset["name"].tolist(),
                             project_subset["markdown_tag"].tolist(),
                             project_subset["class"].tolist())
        project_zip.append({"class":project_class,
                            "project":project_subset,
                            "count":count})
        count+=1
    return project_zip

def get_count():
    return(pandas.read_csv("static/projects.tsv",sep="\t").shape[0])

# Get blog pages
def get_pages():
    posts = [page for page in pages if 'date' in page.meta]

    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return sorted_posts

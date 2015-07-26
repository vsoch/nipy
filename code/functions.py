import pandas

# Get main data for d3
def get_data():
    projects = get_projects()
    n = len(projects)
    m = get_count()
    return projects,n,m
 
# Read in projects from tsv
def get_projects():
    projects = pandas.read_csv("static/projects.tsv",sep="\t")
    projects = projects.sort(columns=["class","name"])
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

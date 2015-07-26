import pandas

# Read in projects from tsv
def get_projects():
    return pandas.read_csv("static/projects.tsv",sep="\t")

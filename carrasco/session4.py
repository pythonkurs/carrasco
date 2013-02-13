import requests
from getpass import getpass as gp
from pandas import DataFrame, Series, concat

def get_commit_history(organization=None, username=None, password=None):
    """Return a DataFrame containing the commit history of all repos from organization.

    It returns a pandas DataFrame in which the columns are the repositories and
    the rows are the commits indexed by time.
    """
    if not organization:
        organization = raw_input("Enter the name of the organization: ")
    if not username:
        username = raw_input("Enter your username: ")
    if not password:
        password = gp("Enter you password: ")

    repos = requests.get(GH_ORG_REPOS.format(org = organization), auth = (username, password)).json()
    data = DataFrame()
    for repo in repos:
        name = repo.get('name')
        commits_list = requests.get(GH_ORG_REPO_COMMITS.format(org = organization, repo = name), auth = (username, password)).json()
        commits = {}
        #If the Git repository is empty, it will return a dict containing the message:
        #{u'message': u'Git Repository is empty.'}, so we check that the returned
        #value is a list. 
        if type(commits_list) == type(list()):
            for commit in commits_list:
                commits[commit.get('commit').get('author').get('date')] = commit.get('commit').get('message')
        data = concat([data, DataFrame(Series(commits.values(), index = commits.keys(), name = name))])
    return data
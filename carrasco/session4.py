import requests
from getpass import getpass as gp
from pandas import DataFrame, Series, concat
from dateutil import parser

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

    BASE_URL = "https://api.github.com/"
    GH_ORG_MEMBERS = BASE_URL + "orgs/{org}/members"
    GH_ORG_REPOS = BASE_URL + "orgs/{org}/repos"
    GH_ORG_REPO_COMMITS = BASE_URL + "repos/{org}/{repo}/commits"

    repos = requests.get(GH_ORG_REPOS.format(org = organization), auth = (username, password)).json()
    data = {}
    for repo in repos:
        name = repo.get('name')
        commits_list = requests.get(GH_ORG_REPO_COMMITS.format(org = organization, repo = name), auth = (username, password)).json()
        commits_messages = []
        commits_dates = []
        #If the Git repository is empty, it will return a dict containing the message:
        #{u'message': u'Git Repository is empty.'}, so we check that the returned
        #value is a list. 
        if type(commits_list) == type(list()):
            for commit in commits_list:
                commits_messages.append(commit.get('commit').get('message'))
                commits_dates.append(parser.parse(commit.get('commit').get('author').get('date')))
            data[name] = Series(commits_messages, index=commits_dates)

    return DataFrame(data)
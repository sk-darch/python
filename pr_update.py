import requests
import json
import sys
import config

from typing import Dict

json_data = None
pr_reviewers = []
pr_title = None
user = config.user
pwd = config.pwd
headers = {"Content-Type": "application/json"}  # type: Dict[str, str]

def get_pullrequest():
    response = requests.get(url, auth=(user,pwd), headers=headers)
    if response.status_code == 200:
        global json_data
        json_data = response.json()
    else:
        return None

def get_title():
    title = json_data
    global pr_title
    pr_title = title['title']
    print pr_title

def get_reviewers():
    review_user = json_data
    for user in review_user['reviewers']:
         users = (user['username'])
         pr_reviewers.append({"username" : str(users)})
    print pr_reviewers


def update_pullrequest(url):
    devops = ["dilippadma", "kvdattada", "sripathik"]
    for dev in devops:
        pr_reviewers.append({"username" : dev })
    data={"title" : pr_title, "reviewers" : pr_reviewers }
    r = requests.put(url, auth=(user, pwd), data=json.dumps(data), headers=headers)
    data = {"content" : { "raw" : "We have found changes in application.properties file hence adding DevOps team as reviewers. please get at least one DevOps team approval before going ahead and marge this PR." }}
    p = requests.post(url + "/comments", auth=(user, pwd), data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    url = sys.argv[1].split("/")
    bit_bucket_owner = url[3]
    bit_bucket_repo_name = url[4]
    bit_bucket_pr_no = url[6]
    url="https://api.bitbucket.org/2.0/repositories/%s/%s/pullrequests/%s" % (bit_bucket_owner, bit_bucket_repo_name, bit_bucket_pr_no)
    get_pullrequest()
    get_title()
    get_reviewers()
    update_pullrequest(url)
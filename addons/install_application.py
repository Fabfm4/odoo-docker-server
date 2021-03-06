import json
import sys
import os
from pprint import pprint


json_file = open("application.json", "r")
json_data = json.loads(json_file.read())
if os.path.exists("./{0}".format(json_data["main_project"])):
    answer = raw_input('Enter your input [Y/n]:')
    if answer != "Y":
        print("OK!")
        #exit()
else:
    print("Cloning main repo ... {0}".format(json_data["main_repo"]))
    os.system("git clone {0} {1}".format(json_data["main_repo"], json_data["main_project"]))
    with  open("./{0}/{1}".format(json_data["main_project"], "oca_dependencies.txt")) as file_oca:
        line = file_oca.readline()
        while line:
            if line[0] != "#":
                repo_content_depends = iter(line.split(" "))
                next_project = next(repo_content_depends)
                next_repo = next(repo_content_depends).strip()
                os.system("git clone {0} {1}".format(next_repo, next_project))
                os.system("cd {0} && git checkout {1}".format(next_project, json_data["name_of_branches"]))
            line = file_oca.readline()

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
            next_project, next_repo = line.split(" ")
            next_repo = next_repo.strip()
            os.system("git clone {0} {1}".format(next_repo, next_project))
            line = file_oca.readline()


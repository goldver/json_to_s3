#!/usr/local/bin/python3
from os.path import expanduser

json_file = "discovery_service.json"
path_to_json = expanduser("~") + "/" + "/tmp/" + json_file
#path_to_repo = input("Enter path to repo after" + expanduser("~") + "/:")


ACCESS_KEY='your_access_key'
SECRET_KEY='your_secret_key'

devops_bucket='bucket-devops'

service_name = input("Service name: ")
repo_name = input("Repo name: ")
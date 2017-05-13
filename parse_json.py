#!/usr/local/bin/python3
import json
from config import *

# appending to json file
def parse_file(path_to_json):
	with open(path_to_json, 'r') as data_file:
		data = json.load(data_file)
		dict = { "git_repo": "git@github.com:gtforge/%s.git" % repo_name}
		data[service_name] = dict  

	with open(path_to_json, 'w') as data_file:    
		json.dump(data, data_file, indent=4) 



#!/usr/local/bin/python3
#chmod +x
import os
import boto3

from config import *
from parse_json import *
from s3_action import *


try:
	download_json(devops_bucket)
except Exception:
	print("Try again...")

try:
	parse_file(path_to_json)
	print("Your Service was successfully added to " + json_file + " file...")
except Exception:
	print("Try again...")

try:
	upload_json(devops_bucket)
except Exception:
	print("Try again...")

def delete_json(path_to_json):
	os.remove(path_to_json)
	
delete_json(path_to_json)	
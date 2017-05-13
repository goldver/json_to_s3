#!/usr/local/bin/python3
from boto3.session import Session
from os.path import expanduser
from config import *

session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')

# Download json file
def download_json(devops_bucket):
	bucket = s3.Bucket(devops_bucket)
	for s3_file in bucket.objects.all():
	    print("Files in this bucket: " + s3_file.key)
	    bucket.download_file(s3_file.key, path_to_json)

# Upload json file
def upload_json(devops_bucket):
	data = open(path_to_json, 'rb')
	s3.Bucket(devops_bucket).put_object(Key=json_file, Body=data)


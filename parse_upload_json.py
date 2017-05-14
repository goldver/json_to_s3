import boto3
import json
import os

s3 = boto3.client('s3')

file_name = "discoveryservice.json"
path_to_json = "/tmp/"
service_name = input("Service name: ")
repo_name = input("Repo name: ")


# downloads json file
def download_file(bucket, file):
    s3.download_file(bucket, file, path_to_json + file)


# appending to json file
def parse_file(path_to_json):
    with open(path_to_json, 'r') as data_file:
        data = json.load(data_file)
        dict = {"git_repo": "git@github.com:goldver/%s.git" % repo_name}
        data[service_name] = dict

    with open(path_to_json, 'w') as data_file:
        json.dump(data, data_file, indent=4)


# uploads json file back
def upload_file(bucket, file):
    with open(file, 'rb') as data:
        s3.upload_fileobj(data, bucket, file_name)


# deletes json file
def delete_json(path_to_json):
    os.remove(path_to_json)


if __name__ == "__main__":
    download_file("bucket-devops", file_name)
    parse_file(path_to_json + file_name)
    upload_file("bucket-devops", path_to_json + file_name)
    delete_json(path_to_json + file_name)
import requests
import json
import getpass

reponame = input("Repository name: ")
description = input("Describe the repo: ")

data = {
"name": reponame,
"description":description,
}

with open('jep.txt', 'w') as filehandle:  
    filehandle.write(json.dumps(data))

with open('jep.txt') as dat:
	data = json.load(dat)

print(data)
username = input("Username: ")
password = getpass.getpass("Password: ")
response = requests.post('https://api.github.com/users/jomppeli/repos',
data, auth=(username, password))
print(response)
print(response.json())

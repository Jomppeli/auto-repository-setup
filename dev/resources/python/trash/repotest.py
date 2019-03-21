import requests
import json
import getpass

#reponame = input("Repository name: ")
#description = input("Describe the repo: ")

#data = {
#"name": reponame,
#"description":description,
#}

#with open('jep.txt', 'w') as filehandle:  
  #  filehandle.write(json.dumps(data))

#with open('fak.txt','r') as dat:
#	data = dat.read()
#data = json.loads(data)
data = '{"name":"testailua"}'
print(data)

username = input("Username: ")
password = getpass.getpass("Password: ")
response = requests.post('https://api.github.com/user/repos?',
data, auth=(username,password))
print(response)
print(response.json())

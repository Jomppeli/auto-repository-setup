import json
import requests

url = "https://api.github.com/jomppeli/repos"
data = {"name": "Hello-World",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "private": false,
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true}

r = requests.post(url=url, data=data)

response = r.json
print(response)

import json
import requests

#url = "https://api.github.com/users/jomppeli/repos"
#url = "https://api.github.com/repos/jomppeli/cheatsheet/readme"

url = "https://api.github.com/repos/jomppeli/cheatsheet/contents/test/test"
headers = {"Authorization":"token tiojhoih"}

data = {
  "message": "my commit message",
  "committer": {
    "name": "Scott Chacon",
    "email": "schacon@gmail.com"
  },
  "content": "bXkgbmV3IGZpbGUgY29udGVudHM="
}

#r = requests.post(url=url, data=data)
#r = requests.get(url=url,headers=headers)
r = requests.put(url=url,headers=headers,data=data)


response = r.json()
print(response)

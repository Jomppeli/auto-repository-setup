import requests
import json
import getpass

data = open('data.txt')

repo = input("repo: ")
username = input("Username: ")
password = getpass.getpass("Password: ")
##data2 = open('pyexample.txt')
##filename2 = "example.py"
##response2 = requests.put('https://api.github.com/repos/%s/%s/contents/test/python/%s'
##% (username,repo,filename2),
##data2, auth=(username, password))
##print(response2)
##
##print(response2.json())

data1 = open('example.txt')
filename = "example.py"

response =requests.put('https://api.github.com/repos/%s/%s/contents/test/%s' 
% (username,repo,filename),
data1, auth=(username, password))
print(response)
print(response.json())

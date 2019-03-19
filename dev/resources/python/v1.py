import requests
import json
import getpass
import subprocess



repo = input("Repository name: ")

data1 = open('example.txt')
username = input("Username: ")
password = getpass.getpass("Password: ")

filename = "readme.md"

response =requests.put('https://api.github.com/repos/%s/%s/contents/test/dev/%s' 
% (username,repo,filename),
data1, auth=(username, password))
print(response)
print(response.json())

data2 = open('pyexample.txt')
filename2 = "example.py"
response2=requests.put('https://api.github.com/repos/%s/%s/contents/test/dev/resources/python/%s'
% (username,repo,filename2),
data2, auth=(username, password))
print(response2)
print(response2.json())

data3 = open('example.txt')
filename3 = "example.json"

response3=requests.put('https://api.github.com/repos/%s/%s/contents/test/dev/resources/data/%s' %(username,repo,filename3),
data3, auth=(username, password))
print(response3)
print(response3.json())
print("Cloning the repository")
subprocess.run(["git","clone","https://github.com/%s/%s" % (username,repo)])
print("\nDone!\nGo ahead and check that the file structure is correct.")


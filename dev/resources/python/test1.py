import requests
import json
import getpass

data = open('data.txt')

filename = input("Filename: ")
username = input("Username: ")
password = getpass.getpass("Password: ")
response = requests.put('https://api.github.com/repos/jomppeli/cheatsheet/contents/docs/%s' % filename, 
data, auth=(username, password))
print(response)
print(response.json())

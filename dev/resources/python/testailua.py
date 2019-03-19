import requests
import json
import getpass


fullPaths = ["projectname/readme.md","projectname/folder/jep.py","projectname/folder/hep.txt"]
def createStructure(fullPaths):
    with open("examplefiles/filenames/files.txt",'r') as exampleFile:
        fileNames = exampleFile.read()
    fileNames = json.loads(fileNames)
    print(fileNames)
    password = getpass.getpass("Password: ")
    for path in fullPaths:
        fileName = path.split("/")
        fileName = fileName[-1]
        fileType = fileName.split(".")
        fileType = fileType[1]
        for key,value in fileNames.items():
            if key == fileType:
                file = value
                data = open(file)
                url = "https://api.github.com/repos/jomppeli/testing/contents/%s" % (path)
                print(url)
                response =requests.put(url,data, auth=("jomppeli", password))
                print(response)
                print(response.json())

createStructure(fullPaths)

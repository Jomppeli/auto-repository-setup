import requests
import json
import getpass
import subprocess
import os


def showExamples():
    # Show the example structures
    # Print every file in /structure folder
    # Take out the file extension (.txt) and print only the name
    
    print("\nChoose a structure: \n")
    files = os.listdir("structures")
    number = 1
    for file in files:
        fileName = file.split(".")
        fileName = fileName[0]
        print(str(number) + ". " + fileName)
        number += 1
    
    project = input(": ")
    chosenFile = files[int(project)-1]
    chosenFile = "structures/" + chosenFile

    # Split every directory and file, and then print the line
    with open(chosenFile,'r') as exampleFile:
        data = exampleFile.read()
        data = data.split("%")
        indx = 0
        while True:
            try:
                print(data[indx])
                indx += 1
            except IndexError:
                break

def createOwn():
    # Get user input of structure creation and use it to create a wanted file structure
    # Join every line and add "%" in between so it follows the same form as the example files
    # e.g -project%--folder%---file
    
    print("\nCreate your own file structure by giving an input and pressing enter.")
    print("Use dashes as an indentation to make nested structures.")
    print("For example:\n-Folder1\n--fileinfolder1.txt\n--folderinsidefolder1\n-Folder2")
    print("To add an file, give it a file extension e.g file.txt.")
    print("Every item without extension is treated as a directory.")
    print("When the structure is ready, press enter.\n")
    print("THE STRUCRUTE HAS TO BE ORDERED FOR IT TO WORK!\n")
    inp2 = ""
    while True:
        inp = input(":")
        if inp == "":
            cn = input("1. Continue\n2. Start over\n:")
            if cn == "1":
                # function to save the created structure to use later
                saveStructure(inp2)
                # Handle the input in different function
                readStructure(inp2)
                break
            if cn == "2":
                break
        inp2 += inp + "%"

def readStructure(structure):
    # this function reads the given structure from string
    # e.g "-project%--file.txt%--folder2%---file2.txt%---folder21%----file21.txt%---folder22%----file22.txt"
    # and creates the full file paths
    # e.g ['project/file.txt', 'project/folder2/file2.txt', 'project/folder2/folder21/file21.txt', 'project/folder2/folder22/file22.txt']
    # then the full file paths can be used to create the files in the github repository.

    structureArray = structure.split("%")
    x = 0
    path = {}
    fullPaths = []
    while True:
        try:
            structureItem = structureArray[x]
            indentation = 0
            # Count the dashes as a indentation, and use them to create the correct paths
            for char in structureItem:
                if char == "-":
                    indentation += 1
                else:
                    break
            itemName = structureItem[indentation:]
            
            # check if the item has a file extension and then treat it as a file
            try:
                file = itemName.split(".")
                fileExtension = file[1]
                previousFolders = indentation - 1
                fullPath = ""

                # iterate over folders and create the wanted structure
                for key, value in path.items():
                    if key <= previousFolders:
                        # Add the folder to the path
                        fullPath += value + "/"
                    if key == previousFolders:
                        # If the indentation value matches the previuousFolders value
                        # Add the filename to the path, and you have a full path
                        fullPath += itemName
                        fullPaths.append(fullPath)

            except Exception:
                # if the item doesn't have a extension
                # treat it as a folder and add it to the path dictionary
                path[indentation] = itemName
                pass
            x+=1
        except Exception:
            break
    createStructure(fullPaths)
        
def createStructure(fullPaths):
    # Combine all the data and create the structure to the repository
    # Get all the example files (jsexample.js etc)
    
    with open("examplefiles/filenames/files.txt",'r') as exampleFile:
        fileNames = exampleFile.read()
    fileNames = json.loads(fileNames)
    
    repo = input("Name of the repository: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Iterate over the full paths
    for path in fullPaths:
        fileName = path.split("/")
        fileName = fileName[-1]
        fileType = fileName.split(".")
        fileType = fileType[1]
        
        # Iterate over the fileNames and if the file extension matches, add the filename to the path
        # If the filetype is .py then find the example file that matches the .py
        for key,value in fileNames.items():
            if key == fileType:
                file = value
                data = open(file)
                url = "https://api.github.com/repos/%s/%s/contents/%s" % (username,repo,path)
                print(url)
                response =requests.put(url,data, auth=(username, password))
                statusCode = response.status_code
                if statusCode == 201:
                    print("Added!")
                #print(response.json())
    print("All done! Enjoy your beautiful file structure. <3")

def saveStructure(structure):
    # Save the structure that the user creates
    # Saves the string to a text file that the user can name
    
    choice = input("Want to save the made structure to be used later?\n1. YES\n2. NO\n: ")
    if choice == "1":
        fileName = input("Name of the file: \n: ")
        file = open("structures/%s.%s"%(fileName,"txt"), "w")
        file.write(structure)
        print(fileName + " saved!")
    if choice == "2":
        print("Structure was not saved.")

def chooseStructure():
    # Choose the structure that the user wants to use
    # Iterates all the filenames from the /structures folder
    # Splits it so it is shown without the file extension (.txt)
    # Reads the chosen file and send the string to readStructure function
    
    print("Choose a structure: \n")
    files = os.listdir("structures")
    number = 1
    for file in files:
        fileName = file.split(".")
        fileName = fileName[0]
        print(str(number) + ". " + fileName)
        number += 1
    
    project = input(": ")
    chosenFile = files[int(project)-1]
    chosenFile = "structures/" + chosenFile

    with open(chosenFile,'r') as exampleFile:
        data = exampleFile.read()
    readStructure(data)

while True:
    # Ask user what du hec it wants to do
    # Loop until user decides to exit
    
    print("\nWhat do you want to do?")
    choice = input("1. Use a predefined structure \n2. Preview the predefined structures\n3. Create your own\n4. Help\n0. Exit\n: ")
       
    if choice == "1":
        # choose predefined structures from /structures folder
        chooseStructure()
        
    if choice == "2":
        #print the example structures
        showExamples()
        
    if choice == "3":
        # Create own file structures
        createOwn()

    if choice == "0":
        #Exit
        break




	

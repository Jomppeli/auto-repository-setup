# auto-repository-setup

<img src="https://img.shields.io/github/tag/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/languages/top/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/repo-size/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/issues/jomppeli/auto-repository-setup.svg?style=for-the-badge">  
<img src="https://forthebadge.com/images/badges/made-with-python.svg"> [![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
  
  
### Script to automatically setup a repository from command line with a wanted file structure.  
**This script uses Githubs API to add folders and files in wanted order and structure to a Github repository in seconds and saves you the manual work of creating folders and files inside eachother.**  
  
Example file structure that can be created in seconds:
- projectname
  - dev
    - test.py
    - site.html
  - documentation
    - docs.md
  - data
    - user_data.json
  - images
    - background.png
  - README.md
  
The script recognizes file extensions and uses the right type of predefined files as placeholders. See below. 
  
[Issues in Kanban view](https://github.com/Jomppeli/auto-repository-setup/projects/2)  
## Why?
Makes the setup of new projects very fast and efficient, and if you do same kind of projects all of the time (e.g webdev), you dont need to do the same things over and over again. Just select or create a wanted file structure and use that every time you start a new project.  
  
  
Parameters:
- repository name (needs to already exist, figuring out the repo creation in next versions)
- wanted file structure (choose from predefined structures or create own. See [examples](#Example-File-structures))
- username/password

## How to use
Copy the `python` folder from `auto-repository-setup/dev/resources` to your computer.  
Go to the same directory in your command line tool and run the script:  
```
python3 test_version_1_01.py
```  

```  
What do you want to do?
1. Use a predefined structure
2. Preview the predefined structures
3. Create your own
4. Help
0. Exit
```  
What to do? Follow the instructions below.   
### [1: Using predefined file structures](#Using-predefined-file-structures)
### [2: Previewing the predefined file structures](#)
### [3: Creating own file structures](#)
---

### 1. Using predefined file structures
Type number 1 and hit enter:  
```  
What do you want to do?
1. Use a predefined structure
2. Preview the predefined structures
3. Create your own
4. Help
0. Exit
```
Every example structure and every structure you create is shown here. The files are in **dev/resources/python/structures** folder.
```
Choose a structure:

1. html-js-php-example
2. python-example
3. teststructure
```
After choosing the structure you like, the script asks for the name of the repository, username and password:  
```
Name of the repository: testing
Username: jomppeli
Password:
```
After that, the script starts to create the file structure to the wanted repository.  
It shows every file it tries to create and if the creation is succesful, it prints out a success message:  
```
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/resources/js/example.js
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/resources/css/example.css
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/resources/php/example.php
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/resources/data/example.json
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/resources/images/example.txt
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/resources/index.php
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/dev/vendor/example.js
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/documentation/example.md
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/README.md
Added!
https://api.github.com/repos/jomppeli/testing/contents/projectname/sketchbook.md
Added!
```
After the structure is created, the script informs the user:  
```
All done! Enjoy your beautiful file structure. <3
```  
  
The created structure in Sublime Text:  
![image_header](https://github.com/Jomppeli/auto-repository-setup/blob/master/dev/documentation/images/4.PNG)
  
The created structure in Github:  
  
![image_header](https://github.com/Jomppeli/auto-repository-setup/blob/master/dev/documentation/images/2.PNG)
  

The script recognizes the given file extensions and uses pre defined example files in the directories.  
For example the JSON file:  
  
![image_header](https://github.com/Jomppeli/auto-repository-setup/blob/master/dev/documentation/images/3.PNG)

### 2. Preview the predefined file structures
Type 2 and hit enter. The script shows all example files and structures that you have created and saved:
```
Choose a structure:

1. example-structure
2. html-js-php-example
3. python-example
4. teststructure
5. the-best
```
After choosing one of the examples, the script then prints out the file structure:
```
-projectname
--dev
---resources
----data
-----example.json
----python
-----example.py
--documentation
---example.md
--README.md
--sketchbook.md
```
From here you can see the whole structure that would be created, if you choose to use the given example.  
### 3. Creating own file structures
Type 3 in the main menu and hit enter. The script gives information about the creation process:
```
Create your own file structure by giving an input and pressing enter.
Use dashes as an indentation to make nested structures.
For example:
-Folder1
--fileinfolder1.txt
--folderinsidefolder1
-Folder2
To add an file, give it a file extension e.g file.txt.
Every item without extension is treated as a directory.
When the structure is ready, press enter.

THE STRUCRUTE HAS TO BE ORDERED FOR IT TO WORK!
```
Follow the instructions and create your own file structure:
```
:-testproject
:--development
:---example.py
:---tasklist.md
:--documentation
:---document.md
:--readme.md
```
The script recognizes the given file extensions and uses predefined example files as placeholders. The example files can be found from **dev/resources/python/examplefiles**. The files are base64 encoded.  
  
Continue and save the structure if needed or start over:
```
1. Continue
2. Start over
```
Save the structure with a wanted filename:
```
Want to save the made structure to be used later?
1. YES
2. NO
:1
Name of the file:
: the-best-structure
the-best-structure saved!
```
The creation is now done. You can use the creation straight away and enjoy your beautiful file structure!





 

## Example File structures
### HTML, Javascript, PHP project
- **Project 1**
  - **dev**
    - **resources**
      - **js**
        - example.js
      - **css**
        - example.css
      - **php**
        - example.php
      - **data**
        - example.xlsx
        - example.json
      - **images**
        - example.png
    - **vendors**
      - library.js
    - index.html/php
  - **documentation**
    - example.md
    - **docs**
      - example.docs
      - example.pdf
  - README.md
  - sketchbook.md  
  - TASKLIST.md???
  
  
### Python project
- **Project 2**
  - **dev**
    - **resources**
      - **data**
        - example.json
      - **python**
        - example.py
  - README.md
  - documentation.md
  - sketchbook.md
  - TASKLIST.md????

# auto-repository-setup
<img src="https://img.shields.io/github/languages/top/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/repo-size/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/issues/jomppeli/auto-repository-setup.svg?style=for-the-badge">  
  
  
Script to automatically setup a repository from command line with a wanted file structure.  
Parameters:
- repository name (needs to exist)
- wanted file structure (choose from predefined structures or create own. See [examples](#Example-File-structures))
- username/password

## How to use
Copy the **python** folder from **auto-repository-setup/dev/resources** to your computer.  
Go to the same directory in your command line tool and run the script:  
```
python test_version_1_01.py
```  
Choose what to do:  
```  
What do you want to do?
1. Use a predefined structure
2. Preview the predefined structures
3. Create your own
4. Help
0. Exit
```
1. Use predefined structure  
Every example structure and every structure you create is shown here 
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
It shows every file it tries to create and if the creation is succesful, it prints out a message.  
After the structure is created, the script informs the user:
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
All done! Enjoy your beautiful file structure. <3
```
The created structure in Github:  
  
![image_header](https://github.com/Jomppeli/auto-repository-setup/blob/master/dev/documentation/images/2.PNG)
  

The script recognizes the given file extensions and uses pre defined example files in the directories.  
Example the JSON file:  
  
![image_header](https://github.com/Jomppeli/auto-repository-setup/blob/master/dev/documentation/images/3.PNG)






 

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

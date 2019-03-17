# auto-repository-setup
<img src="https://img.shields.io/github/languages/top/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/repo-size/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/issues/jomppeli/auto-repository-setup.svg?style=for-the-badge">  
  
  
Script to automatically setup a repository from command line with a wanted file structure.  
Parameters:
- repository name
- wanted file structure (html/python project)
- public/private
- description
- readme
- more

Goal is to do it with Python3 using the Github API. 
  
[API documentation](https://developer.github.com/v3/) from Github.  
[My synopsis]().

## First version (add the file structure to a existing repository)
Script that adds the wanted file structure to a existing repository, so there is no need to create the repo form command line in this version.  
  
Test different approaches:
- Cloning the repo and 
- mkdir/touch creating the structure
- or use the Github API to create the file structure
  
## Script pipeline
- Take the needed parameters from the user
- Add the parameters to a text file (json parse not working)
- Add a new repository with the parameters that user inputs
- Add the directories and example files

## File structure
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

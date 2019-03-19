# auto-repository-setup
<img src="https://img.shields.io/github/languages/top/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/repo-size/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/issues/jomppeli/auto-repository-setup.svg?style=for-the-badge">  
  
  
Script to automatically setup a repository from command line with a wanted file structure.  
Parameters:
- repository name (needs to exist)
- wanted file structure (choose from predefined structures or create own)
- username/password


Goal is to do it with Python3 using the Github API. 
  
[API documentation](https://developer.github.com/v3/) from Github.  

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

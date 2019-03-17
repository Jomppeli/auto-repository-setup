# auto-repository-setup
<img src="https://img.shields.io/github/languages/top/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/repo-size/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/issues/jomppeli/auto-repository-setup.svg?style=for-the-badge">  
  
Script to automatically setup a repository from command line with a wanted file structure. Takes project type (wanted file structure), repository name, description and a readme info as a parameters. 
  
Done with Python3 using the Github API. 
  
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
  - full-documentation.md
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

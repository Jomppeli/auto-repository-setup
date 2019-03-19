# auto-repository-setup
<img src="https://img.shields.io/github/languages/top/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/repo-size/jomppeli/auto-repository-setup.svg?style=for-the-badge"> <img src="https://img.shields.io/github/issues/jomppeli/auto-repository-setup.svg?style=for-the-badge">  
  
  
Script to automatically setup a repository from command line with a wanted file structure.  
Parameters:
- repository name (needs to exist)
- wanted file structure (choose from predefined structures or create own)
- username/password

### How to use
Copy the **python** folder from **auto-repository-setup/dev/resources** to your computer.  
Go to the same directory in your command line tool and run the script:  
```
python test_version_1_01.py
```  
 

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

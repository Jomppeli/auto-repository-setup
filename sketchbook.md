## #7
Pushed test version 1.01 to production. 

## #6 
Added some issues for the future.

## #5
Made a new repo for testing named "testing". Also started to document the versions and features to the documentation directory.

## #4 ADDED TO ISSUES
Make it possible to write the wanted file structure when asked and make the script to follow that.  
For example just writing simply the directory names and file names to a file with proper indetations and reading from the file.  
  
Example:
- directory
  - file.txt
  - directory
    - file.pdf
  
Then the script reads that from the file and creates the wanted file structure.

## #3 **Added to issues**
**TODO**:  
Write a script that creates the wanted file structure to a already existing repository. So no need to create the repository from the command line, just create the file structure.  
Try it out by using the API and also just using mkdir and touch commands.

## #2 
Did some test scripts and shit. Legit request keeps givin me 404 so that needs to be sorted out. 
The repotest.py and this curl:  
curl -XPOST -H "Authorization: token <token>" https://api.github.com/jomppeli/repos -d '{"name":"test"}'
{
  "message": "Not Found",
  "documentation_url": "https://developer.github.com/v3"
}  
Both give 404 so that's a problem.
## #1
Setup the repos file structure and write down the used file structure options to readme.

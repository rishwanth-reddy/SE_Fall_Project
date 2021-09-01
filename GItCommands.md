# Basic Terminal Commands

`history` –> to check the commands used prior

`mkdir <foldername>` -> to create directory/folder

`pwd` -> to check the current directory path

`ls -la` -> to fetch the list of files 

`rm <filename>` -> remove/delete file

`rm -rf <foldername>` -> remove directory

`ctrl + c` –> to end the wrong input

`vi <filename>` -> to open new file in terminal
 `i` -> insert into file
 `esc` -> readmode
 `:wq!` -> save and quit [without w – file quits, doesn’t save]


# VSCode Commands

`ctrl + tilde` -> to open the terminal in VS code

`code <repository name>` -> to open the project in VS code

# GitHub Commands

`git clone <clone url from git>` -> clone the git repository with editor using terminal

`git status` -> to check the recent activity

`git add <filename>` -> staging

`git commit -m “<message>”` -> commit

`git push` –> push from local to remote

`git pull` -> to pull the changes from the remote to local

### Git Branch Commands

`git pull origin <branch name>` -> Pull from origin <branch name>

`git push origin <branch name>` -> -> Push to origin <branch name>

`git checkout -b "branchname"` -> to create new branch locally

`git checkout <branchname>` -> to open existing branch

### Git Tag Commands

`git tag <tag-name>` -> to create tag locally

`git tag <tag-name> -a -m “msg”` -> to create tag locally with message

`git push origin –tags` -> this will push all the tags from local to remote

`git push origin <tagname>` -> this will push just one tag

NOTE: Tag names and branch names should be unique
NOTE: If u want to use old tag name for new commit then delete old tag using ->  
`git tag –delete <tag-name>` [or] `git tag -d <tag-name]` [locally]
`git push -d origin <tag-name>` -> to delete remote


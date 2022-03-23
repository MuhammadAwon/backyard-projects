## Essentials Commands for GitHub

### First time:
- $ git config --global user.name “John Doe” (To set Username)
- $ git config --global user.email “john@doe.org” (To set UserEmail)
- $ git config --global color.ui auto (To automate the colour Scheme)

### Whenever you have to push material:
- $ git status (To check status of Track & untrack files i.e. staging area)
- $ git add -A <b>OR</b> $ git add . <b>OR</b> $ git add fileName (To add changes to git)
- $ git commit -m “Initial commit" (To Commit your changes)
- $ git push -u origin <branchname> (To push data to GitHub)

### Branching:
- $ git branch <branchname> (To create a branch)
- $ git branch -d <branchname> (To delete branch )
- $ git checkout <branchname> (To move from one branch to another)

## BOOK (VERSION CONTROL SYSTEM)

### Chapter1:
- $ git config --global user.name “John Doe” (To set Username)
- $ git config --global user.email “john@doe.org” (To set UserEmail)
- $ git config --global color.ui auto (To automate the colour Scheme)
- $ cd <path/to/project/folder> (To change the directory)
- $ git init (To initialize the repository)
- $ git init --bare (initialize Git without making .git folder and place its files outside)
- $ ls -la (To list down all the contect in your Working Directory)
- $ git add -A <b>OR</b> $ git add . <b>OR</b> $ git add fileName (To add changes to git)
- $ git commit -m “Initial commit" (To Commit your changes)
- $ cd your/development/folder/ (To change your directory)
- $ git clone https://github.com/gittower/git-crash-course.git (To clone data from GitHUb)
- $ git status (To check status of Track & untrack files i:e Stangging area)
- $ git add new-page.html index.html css/*  (To add Specified name to Git )
- $ git commit -m “Implement the new login box” (To Commit your changes)
- $ git log (To check you activity History)

### Chapter2:
- $ git branch contact-form (To create branch by name of contact-form)
- $ git branch -v (To list out number of branches with little detail)
- $ git status (To check status of track & untrack files i.e. staging area)
- $ git stash (To add files as temporary file to clipborad without uploading it into GitHub)
- $ git status (To check status of track & untrack files i.e. staging area)
- $ git stash list (To list out all stash that you added in clipborad)
- $ git checkout contact-form (To move from one branch to another)
- $ git add contact.html (To add files to commit)
- $ git commit -m "Add new contact form" (To Commit your changes)
- $ git log (To check you activity history)
- $ git checkout master (To move from one branch to another)
- $ git merge contact-form (To merge files of contact-form NOTE:To merge files you must have to specify branch in main to add contact branch to main)
- $ git log(To check you activity history)

### Chapter3:

- $ git remote add origin https://github.com/ImGit/test1.git (To set origin where you want to push your data)
- $ git remote -v (Show number of remote repositories connected to your working directory)
- $ git branch -va (work same as "$ git remote -v" by giving some more details)
- $ git fetch origin master (To fetch the changes from main repository)
- $ git fetch origin (To fetch file from origin NOTE: origin is the main directory the store by GitHub in orgin)
- $ git log origin/master  (To check you activity history of main branch)
- $ git pull (To pull file from origin)
- $ git checkout <branchname> (To move from one branch to another)
- $ git push -u origin <branchname> (To push data to GitHub)
- $ git branch -vva (work same as "$ git remote -va" by giving some more details)
- $ git branch -d <branchname> (To delete branch )
- $ git branch -dr origin/<branchname> (to delete branch from origin/base repository)
  </br>
- $ git remote add origin <url> (To set origin where you want to push your data)
- $ git remote add origin <"clone"> -f
- $ git push origin main (To push data to GitHub) <b>OR</b> git push origin main -f (To push data to GitHub forefully NOTE: we always try to avoid use of this branch)
- $ git clone <reponame> (To clone data from GitHUb)
- $ git pull origin main (To pull file from origin NOTE: origin is the main directory the store by github in orgin)
  </br>
- $ git push -u origin <branch> -f (push local branch on server)
- $ git push --all -u (push all things on remote server)
- $ git pull --all (pull all data from server)

If you have clone remote repository you can rename by following steps:
- git branch -m master main
- git fetch origin
- git branch -u origin/main main


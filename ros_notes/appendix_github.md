## github 

-[] make your account, review Terminology
-[] install git with `$sudo apt-get install git`
-[] create a local git repo
-[] add a new file to the repo

We'll be using the terminal for all this. Your IDE will have similar commands. 
If you dont want the terminal, github has a tutorial that's better than doing it in the terminal. I made this tutorial not because its more efficient, but because I thought it would be easy.

![link to githubs tutorial](https://guides.github.com/activities/hello-world/)

**Create a local git repository :**
- create a folder where you will place your repo
- type `$ git init` inside your folder
```
$ cd ~/Desktop
$ mkdir myproject
$ cd myproject/
$ git init
```

**Adding files**
- we will create and add a file for this example
- the important part is `git status` 
- `git status` lets you see what changes git has noticed you have made
- git will not officially keep track of any file unless you `add` it
```
$ touch test_file.txt
$ git status
$ git add test_file.txt
```

**Commit**
- when you use `git add <file_name>` , git stages the files for upload
- `-m` is for the message you want to add
- it should contain info regarding features\bugfix\ticket\etc...
```
git commit -m "This comment is public, used to indicate progress/changes"
```

**Branch**
- branches are like save-points in videogames
- you can have as many branches as you want but they all merge to the master
- you can move back and forth between branches
- you `checkout` a branch if you want to make changes to it
- if a branch does not exist, git creates one for you
- run `git branch` to confirm and check your branches
- there will be an asterist next to your branch
- you can switch to the master branch, make changes and merge it to your new branch
```
git checkout -b new_branch_name

git branch
```

**our first repo on git**
- ![create a new repository](https://cdn2.hubspot.net/hub/51294/hubfs/Git_101_Screenshot1-2.png?width=671&height=141&name=Git_101_Screenshot1-2.png)
- ![add name of repo and brief description](https://cdn2.hubspot.net/hub/51294/hubfs/Git_101_Screenshot_2-1.png?width=671&height=418&name=Git_101_Screenshot_2-1.png)
- git will ask if creating a new repo, or adding from a local source
- finish creating your repository
- select `...or push an existing repository from the command line` for this example

**combining our local repo with github.com**
- [] we have created a local git repo
- [] we have created a new repository on github.com
- [] we copied the link to our repo from github.com
- [] we learn the `push` command
- origin is the default filename git created for your repo
- you use a remote login to add the link to your repo on your local git repo
- you can then `push` your to the cloud 
```
git remote add origin <the link of your repo>
git push -u origin master
```
here we *remote*-ly connect to github, *add* the *origin* found at your *link*. Afterwards we *push* that *origin* to our *master*. 

**Push**
- push the commit in your branch from earlier to your new repo on github
- anyone you are sharing with can now see your changes
- we can now push the changes we made to our new_branch_name earlier
```
git push origin new_branch_name
```
Github will place it in its proper location now that it knows the structure of your folder. Your files on your local drive will remain the same but you can pull any file from any brach on github. If you make a mistake, just *pull*.

**Pull**
- `git pull` is shorthand for `git fetch` follewed by `git merge FETCH_HEAD`
- fetch : fetch branches from repo's along with their objects
- merge : merge the retrieved branch heads into the current branch
- `git pull [<options>] [<repository>] [<refspec>]`

**Merge**
- just like merge sort, there's some conditions we need to keep track of when merging.
- changes from the names commits are merged into the current branch
- conflicts are handled on a case-by-case basis
- as we run into problems, we can add them to a list of 'lessons learned' 
```
git merge [-n] [--stat] [--no-commit] [--squash] [--[no-]edit]
    [--no-verify] [-s <strategy>] [-X <strategy-option>] [-S[<keyid>]]
    [--[no-]allow-unrelated-histories]
    [--[no-]rerere-autoupdate] [-m <msg>] [-F <file>] [<commit>…​]
git merge (--continue | --abort | --quit)
```


Terminology:
**Snapshots**
- records of what your files look like at a given point in time
- you decide when to take a snapshot
- you can go back to visit previous snapshots
- the snapshots you made will still remain
**Commit**
- creates a \'snapshot\' along with a comment 
- comments you make will be permanent and visible to everyone
- each commit contains (3) pieces of info:
    + what changed, how it was made, etc..
    + a reference to the 'parent commit'
    + a hash-code name
**Repositories**
- all your work is stored in a repository (repo)
- repo's can live on the cloud or locally on any storage
- copying a repo from a server is referred to as *cloning*
- *pulling* changes is the process of downloading commits that don't exist on your machine
- *pushing* changes adds your local edits to the remote repository
**Branches**
- all commits exist on a branch
- there can be many branches
- the main branch is called the *master branch*
- each child points to its own parent
- the head of the list points to the master branch
- branch off of the master to make any changes to the project
- merge with the master branch when you are done
**Merging**
- this is when you'll handle conflits
- //Stopping here... Continue Me

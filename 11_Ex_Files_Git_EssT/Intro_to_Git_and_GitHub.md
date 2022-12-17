# Week 01: Introduction to Git and Github

## Before version control

### Diffing files
diff tool: used to show the differences between two files (work line by line)
	https://git-scm.com/docs/git-diff
	

### Applying changes
diff -u old_file new_file > change.diff 
	(diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output)

patch old_file.py < change.diff: applies the changes contained in a diff file to another file


### Practical Application of diff and patch
cp disk_usage.py disk_usage_original.py
cp disk_usage.py disk_usage_fixed.py

diff -u disk_usage_original disk_usage_fixed > disk_usage.diff
patch disk_usage.py < disk_usage.diff

### diff and patch Cheat Sheet

#### diff
diff is used to find differences between two files. On its own, it’s a bit hard to use; instead, use it with diff -u to find lines which differ in two files:

#### diff -u
diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output. See below:

		~$ cat menu1.txt 
		Menu1:

		Apples
		Bananas
		Oranges
		Pears

		~$ cat menu2.txt 
		Menu:

		Apples
		Bananas
		Grapes
		Strawberries

		~$ diff -u menu1.txt menu2.txt 
		--- menu1.txt   2019-12-16 18:46:13.794879924 +0900
		+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
		@@ -1,6 +1,6 @@
		-Menu1:
		+Menu:
		 
		-Apples
		-Bananas
		-Oranges
		-Pears
		+Grapes
		+Strawberries

## Version Control Systems (VCS)

### What is version control?
What does a version control system do? It keeps track of changes we do to our files.
By keeping track of the changes that we make to our files, a VCS lets us know when a file changed, who changed it, and also lets us easily roll back those changes.

We can make edits to multiple files and treat that collection of edits as a single change, which is commonly known as a **commit**.

### Git (Version Control System)
Git it's a distributed VCS, which means that each developer has a full copy of the repository. Repositories can be used by as many developers as needed.

##### More information about Git
	- https://git-scm.com/doc

	- https://www.mercurial-scm.org/

	- https://subversion.apache.org/

	- https://en.wikipedia.org/wiki/Version_control
	
### Version Control System Quiz
1. How can a VCS (Version Control System) come in handy when updating your software, even if you’re a solo programmer?
	- Git retains local copies of repositories, resulting in fast operations. Git's distributed architecture means each person contributing to a repository retains a full copy of the repository locally.
	- If something breaks due to a change, you can fix the problem by reverting to a working version before the change.
	- Git allows you to review the history of your project.
	
2. Who is the original creator and main developer of the VCS (Version Control System) tool Git?
	- Linus Torvalds developed Git in 2005 to better facilitate the process of developing the Linux kernel with developers across the globe.
	
3. *Version control* is a feature of a software management system that records changes to a file or set of files over time so that you can recall specific versions later.

4. A *commit* is a collection of edits which has been submitted to the version control system for safe keeping.

5. Within a VCS, project files are organized in centralized locations called *repositories* where they can be called upon later.

## Using Git 

### First Steps with Git
git config --global user.email "me@example.com" (--global is used to set config to all git repository)
git config --global user.name "my_name"

		mkdir checks
		cd checks 
		git init (initiate a repository)

		ls -la
		ls -l .git/

What are git directory and the working tree? 
The **git directory** contains all the changes and their history and the **working tree** contains the current versions of the files.
The git directory acts as a database for all the changes tracked in Git and the working tree acts as a sandbox where we can edit the current versions of the files.

		cp ../disk_usage.py
		ls -l
		git add disk_usage.py 
		git status (get some information about the current workig tree and pending changes)
		git commit
		
*Staging area (Index)*: A file maintained by Git that contains all of the information about what files and changes are going to into your next commit.

### Tracking Files (Git Workflow)
When we working with Git our files can be tracked or untracked. Tracked files are part of the snapshots, while untracked files aren't.
Each tracked file can be in one of three main states: *modified*, *staged* or *committed*.

#### Modified
Means that we have made changes to our file that haven't committed yet (adding, modigying, deleting).

#### Staged
Add files that are ready to be committed to the project.

#### Committed 
When we stored those changes in the VCS.
		
		git add disk_usage_changed.py (stage area)
		git commit -m "stored changes in the vcs"
		
git log: use to review the commit history of the project. git log will give us information about the author of each commit, its timestamp, and each commit message.
git config -l: git config -l is used to check the current user configuration.
git status: git status is used to retrieve information about changes waiting to be committed.

# Week 02: Using Git Locally

## Advanced Git interaction

### Skipping the Staging Area
git commit -a: A shortcut to stage any changes to tracked files and commit them in one step. (Does not work to new files.)
		git commit -a -m "A shortcut to stage any changes to tracked files and commit them in one step."
		
Git uses the HEAD alias to represent the currently checked-out snapshot of your project.

### Getting More Information About Our Changes
git log -p(atch): also shows the actual lines that changed in eache commit.
git show <commit_id>: taking the commit ID, git show will show information about the commit and its associated patch.
git log --stat
git diffgit diff --staged

### Deleting and Renaming Files
Removing a file:
		git rm process.py
		git status
		git commit -m "Delete unneeded file"
		
Rename a file:
		git mv disk_usage.py check_free_space.py
		git commit -m "New name for disk_usage.py"
		
.gitignore: inside this file, we'll specify rules to tell git which files to skip for our repo.
		echo .DS_STORE > .gitignore
		ls -la
		git add .gitignore
		git commit -m "Add a gitignore file, ignoring .DS_STORE files"
		
### Advanced Git Cheat Sheet
Command           | Explanation 

git commit -a     | Stages files automatically

git log -p        | Produces patch text

git show          | Shows various objects

git diff          | Is similar to the Linux `diff` command, and can show the differences in various commits

git diff --staged | An alias to --cached, this will show all staged files compared to the named commit

git add -p        | Allows a user to interactively review patches to add to the current commit

git mv            | Similar to the Linux `mv` command, this moves a file

git rm            | Similar to the Linux `rm` command, this deletes, or removes a file

![Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf) 

**.gitignore files**
.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at: https://git-scm.com/docs/gitignore.

## Undoing Things

### Undoing Changes Before Committing
git checkout <file>: use to discard changes in working directory. It reverts changes to modified files before they are staged.
		git checkout all_checks.py
		git status
		
git reset HEAD <file>: use to unstage file
		git add *
		git status
		git reset HEAD output.txt
		git status
		git commit -m "message"
		
### Amending Commits
git commit --amend: used to overwrite the previous commit. git commit --amend allows us to modify and add changes to the most recent commit. (AVOID AMENDING COMMITS THAT HAVE ALREADY BEEN MADE PUBLIC. USE JUST IN LOCAL COMMITS!)
		git commit -m "Add two files"
		git add gather-info.sh
		git commit --amend
			"Add two new files"
			
### Rollbacks
git revert: with *git revert*, a new commit is created with inverse changes. This cancels previous changes instead of making it as though the original commit never happened.
		git commit -a -m "Add call to disk_full function"
		git revert HEAD
			"the disk_full is undefined"
		git log -p -2
		
### Identifying a Commit
SHA1 HASH Numbers: "You can verify the data you get back out is the exact same data you put in." - Linus Torvalds.
About SHA1 HASH Numbers:
	- They are composed of 40 characters.
	- They are created using the commit message, date, author, and the snapshot taken of the working tree.
	- They provide the consistency that is critical for distributed systems such as Git.
		git log -1
			HASH + SHA1
		git log -2
		gt show <id>
		git revert <id>
		
### Git Revert Cheat Sheet
- *git checkout* is effectively used to switch branches.

- *git reset* basically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.

There are some other useful articles online, which discuss more aggressive approaches to resetting the repo.

- *git commit --amend* is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

- *git revert* makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a few ways you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1. 

Feel free to read more here:

	- https://en.wikipedia.org/wiki/SHA-1

	- https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/
	
### Some questions and good practices
1. Let's say we've made a mistake in our latest commit to a public branch. Which of the following commands is the best option for fixing our mistake?
	*git revert*. git revert will create a new commit to reverse the previous one, and is the best option for undoing commits on public branches.
	
2. If we want to rollback a commit on a public branch that wasn't the most recent one using the revert command, what must we do?
	use the commit ID at the end of the git revert command. The commit ID is a 40-character hash that identifies each commit.
	
3. What does Git use cryptographic hash keys for?
	To guarantee the consistency of our repository. Git doesn't really use these hashes for security. Instead, they’re used to guarantee the consistency of our repository.
	
4. What does the command git commit --amend do?
	Overwrite the previous commit. The command git commit --amend will overwrite the previous commit with what is already in the staging area.
	
5. How can we easily view the log message and diff output the last commit if we don't know the commit ID?
	*git show*. The git show command without an object parameter specified  will default to show us information about the commit pointed to by the HEAD (the currently snapshot).
	
## Branching and Merging

### What is a branch?
Branch: A pointer to a particular commit.

The deafult branch that git creates for you when a new repository is initialized is called **master**.

The purpose of organizing repositories into branches is useful to enable changes to be worked on without disrupting the most current working state. By creating a new branch, we can experiment without breaking what already works.

### Creating New Branches
git branch:
		git branch
		git branch new-feature
		git branch
		git checkout new-feature
		git branch
		git checkout -b even-better-feature (Creates a new branch and switches to it.)
		
		git add free_memory.py
		git commit -m "Add free_memory"
		
### Working with Branches
*git checkout* switch branches by updating the working tree to match the selected branch.
		git status
		ls -l (working tree)
		git checkout master
		git log -2
		
git branch -d <branch-name>:
		git branch -d new-feature
		git branch
		
### Merging
*Merging* is the term that Git uses for combining branched data and history together.
**git merge**:
		git merge even-better-feature (merge into master branch)
		
When we merge two branches both branches are pointed at the same commit. Merging combines branched data and history together.

### Merge Conflicts
The advantage of Git throwing a merge conflict error in cases of overlap it's prevents loss of work if two lines overlap.
If two lines have differences Git is unsure about, it's best we decide than risk losing work forever.

git log --graph --oneline

git merge --abort: stop the merge and reset the files in your working tree back to the previous commit before the merge ever happened.

### Git Branches and Merging Cheat Sheet
Command                   | Explanation

git branch                | Used to manage branches

git branch <name>         | Creates the branch

git branch -d <name>      | Deletes the branch

git branch -D <name>      | Forcibly deletes the branch

git checkout <branch>     | Switches to a branch.

git checkout -b <branch>  | Creates a new branch and switches to it.

git merge <branch>        | Merge joins branches together. 

git merge --abort         | If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.

git log --graph --oneline | This shows a summarized view of the commit history for a repo.

# Week 03: Working with Remotes

## Introduction to GitHub

### What is GitHub?
GitHub provides free access to a Git server for public and private repositories.

### Basic Interaction with GitHub
git clone 
git push: The git push command gathers all the snapshots we've taken and sends them to the remote repository.

### Basic Interaction with GitHub Cheat-Sheet

Command        |	Explanation & Link

git clone URL  |	Git clone is used to clone a remote repository into a local workspace (https://git-scm.com/docs/git-clone)

git push       |	Git push is used to push commits from your local repo to a remote repo (https://git-scm.com/docs/git-push)

git pull       |	Git pull is used to fetch the newest updates from a remote repository (https://git-scm.com/docs/git-pull)

git config --global credential.helper cache

This can be useful for keeping your local workspace up to date.

	- https://help.github.com/en/articles/caching-your-github-password-in-git

	- https://help.github.com/en/articles/generating-an-ssh-key
	
## Using a Remote Repository

### What is a remote?
If the master repository receives a major update since the last local copy was synced Git will let you know it's time for an update.

### Working with Remotes
If we want to make a change to a remote branch we must we pull the remote branch, merge it with the local branch, then push it back to its origin.

### Fetching New Changes
The main difference between git fetch and git pull is that *git fetch* fetches remote updates but doesn't merge; *git pull* fetches remote updates and merges.

### Updating the Local Repository
As long as there are no conflicts, Git will move the current branch tip up to the target branch tip and combine histories of both commits.

### Git Remotes Cheat-Sheet
Command                |	Explanation & Links

git remote             |	Lists remote repos

git remote -v          |	List remote repos verbosely

git remote show <name> |	Describes a single remote repo

git remote update      |	Fetches the most up-to-date objects

git fetch              |	Downloads specific objects

git branch -r          |	Lists remote branches; can be combined with other branch arguments to manage remote branches

**Some questions**
1. In order to get the contents of a remote branch without automatically merging we use *git remote update*.
git remote update will fetch the contents of all remote branches and allow us to merge the contents ourselves.

2. If we need to find more information about a remote branch *git remote show origin* will help us.

3. *git fetch* will download remote updates, such as objects and refs, from the remote branch, without merging the content with your current workspace automatically.

4. An explicit merge creates a new merge commit. This alters the commit history and explicitly shows where a merge was executed.

5. *git pull* automatically merges the remote branch with the current branch.

## Solving Conflicts

### Pushing Remote Branches
*git push -u origin refactor_branch*: push the changes made in the refactor_branch to the remote branch origin.

### Rebasing Your Changes
*git rebase <branch_name>* move the current branch on top of the branch_name branch. This makes debugging easier and prevents three-way merges by transferring the completed work from one branch to another.

Rebasing instead of merging rewrites history and maintains linearity, making for cleaner code.

### Some Best Practices for Collaboration
* Always synchronize your branches before starting any work on your own.

* Avoid having very large changes that modify a lot of different things.

* When working on a big change, it makes sense to have a separate feature branch.

* Regularly merge changes made on the master branch back onto feature branch.

* You shouldn't rebase changes that have been pushed to remote repos.

* Have good commits messages.

### Conflict Resolution Cheat Sheet
GitHub documentation on how to handle with merge conflicts when they happen:

	* https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts

	* https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line
	
# Week 04: Collaboration

## Pull Requests

### A Simple Pull Request on GitHub
**Forking**: a way of creating a copy of the given repository so that it belongs to our user.

**Pull Request**: a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.

rebase -i <branch>
git push -f
git log --graph --oneline --4

### Git Fork and Pull Request Cheat Sheet
- https://help.github.com/en/articles/about-pull-request-merges

### Some questions
1. What is the difference between using squash and fixup when rebasing?
Squash combines the commit messages into one. Fixup discards the new commit message. The fixup operation will keep the original message and discard the message from the fixup commit, while squash combines them.

2. What is a pull request?
A request sent to the owner and collaborators of the target repository to pull your recent changes. You send a pull request to the owner of the repository in order for them to incorporate it into their tree.

3. Under what circumstances is a new fork created?
When you want to experiment with changes without affecting the main repository. For instance, when you want to propose changes to someone else's project, or base your own project off of theirs.

4. What combination of command and flags will force Git to push the current snapshot to the repo as it is, possibly resulting in permanent data loss?
*git push -f*. git push with the -f flag forcibly replaces the old commits with the new one and forces Git to push the current snapshot to the repo as it is. This can be dangerous as it can lead to remote changes being permanently lost and is not recommended unless you're pushing fixes to your own fork (nobody else is using it) such as in the case after doing interactive rebasing to squash multiple commits into one as demonstrated.

5. When using interactive rebase, which option is the default, and takes the commits and rebases them against the branch we selected?
*pick*. The pick keyword takes the commits and rebases them against the branch we have chosen.

## Code Reviews

### What are code reviews?
**Code review** is going through someone else's code, documentation, or configuration and checking that it all makes sense and follows the expected patterns.

*Nit*: A trivial comment or suggestion

### More Information on Code Reviews
* http://google.github.io/styleguide/

* https://help.github.com/en/articles/about-pull-request-reviews

* https://medium.com/osedea/the-perfect-code-review-process-845e6b* a5c31

* https://smartbear.com/learn/code-review/what-is-code-review/

## Managing Projects

### Continuous Integration (CI)
*CI* will build and test our code every time there's a change.

* **Pipelines**: specify the steps that need to run to get the result you want.
	- *Artifacts*: the name used to describe any files that are generated as part of the pipeline.
	
### Additional Tools
* https://arp242.net/diy.html 

* https://help.github.com/en/articles/closing-issues-using-keywords

* https://help.github.com/en/articles/setting-guidelines-for-repository-contributors 

* https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html

* https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/

* https://docs.travis-ci.com/user/tutorial/

* https://docs.travis-ci.com/user/build-stages/































































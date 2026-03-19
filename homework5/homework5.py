# 3.1 Vocabulary Review
 
# 1. Git vs. GitHub
# Git is a version control system used to track changes in code.
# GitHub is an online platform that hosts Git repositories and allows collaboration.

# 2. Terminal vs. Command Line
# The terminal is the application you use to interact with your computer using text.
# The command line is the interface where you type commands inside the terminal.

# 3. Local vs. Remote Repository
# A local repository is stored on your computer.
# A remote repository is stored online (like on GitHub).

# 4. Version Control
# Version control is a system that tracks changes to files over time and allows you to revert to previous versions.

# 5. Staging Area
# The staging area is where changes are prepared before being committed in Git.

# 6. git add
# Adds files to the staging area.

# 7. git commit
# Saves a snapshot of changes in the repository with a message.

# 8. git push
# Uploads local commits to a remote repository.

# 9. git status
# Shows the current state of the repository (changes, staged files, etc.).

# 10. git pull
# Downloads changes from a remote repository and merges them into the local one.

# 11. pwd
# Prints the current working directory.

# 12. ls
# Lists files and folders in the current directory.

# 13. cd
# Changes the current directory.

# 14. nano
# Opens a file in the nano text editor.

# 15. touch
# Creates a new empty file.

# 16. mv
# Moves or renames files and folders.

# 17. rm
# Deletes files or directories.

# 18. cat
# Displays the contents of a file in the terminal.



# 3.2 Directory Tree Questions

# 1. What command tells you your current working directory?
# pwd

# 2. What command lists all files in your current working directory?
# ls

# 3. What commands move to brianna_repo and pull latest changes?
# cd ../brianna_repo
# git pull

# 4. How to move homework.py to the homework/ folder?
# mv homework.py ../judy_decal/homework/

# 5. How to move yourself to the same repository as homework.py?
# cd ../brianna_repo

# 6. How to view contents of homework.py in terminal?
# cat homework.py

# 7. What commands save changes and push to remote repository?
# git add .
# git commit -m "message"
# git push

# 8. How to fix the git error and what does it mean?
# Commands:
# git pull
# git push

# Meaning:
# The error means the remote repository has changes that are not in your local repository.
# Judy tried to push without first pulling the latest updates.

# 9. What absolute path moves you to Recents/?
# cd ~/Recents



# 4.1 Data Types
def checkDataType(x):
	return type(x).__name__

# 4.2 Conditionals
def evenOrOdd(x):
	if x % 2 == 0: 
		return "Even"
	else:
		return "Odd"

# 5 Loops
def sumWithLoop(numbers):
	total = 0
	for num in numbers:
		total += num
	return total

# 6.1 Lists
def duplicateList(lst):
	new_list = []
	for item in lst:
		new_list.append(item)
		new_list.append(item)
	return new_list

# 6.2 Debugging
def square(num):
	return num * num

print(sumWithLoop([1, 2, 3, 4, 5]))
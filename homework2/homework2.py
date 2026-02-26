# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# The difference between Git, GitHub, and Git Bash is as follows:
# - Git is a version control system that allows developers to track changes in their code and collaborate with others. It is a command-line tool that can be used to manage code repositories locally on a computer or remotely on a server.
# - GitHub is a web-based platform that provides hosting for Git repositories. It allows developers to store their code online, collaborate with others, and manage their projects using Git. GitHub also offers additional features such as issue tracking, pull requests, and project management tools.
# - Git Bash is a command-line interface that provides a Unix-like environment on Windows. It allows users to run Git commands and use other Unix tools in a terminal window. Git Bash is often used by developers who prefer a command-line interface for working with Git on Windows.

# 2) What’s the difference between the terminal and the command line?
# The terminal is a graphical interface that allows users to interact with the operating system through text commands. The command line is the interface within the terminal where users type commands. In essence, the terminal is the application window, and the command line is where commands are entered within that window.

# 3) How does Windows PowerShell differ from Git Bash?
# Windows PowerShell is a task automation and configuration management framework developed by Microsoft. It provides a command-line interface and scripting language for managing Windows systems. Git Bash, on the other hand, is a Unix-like environment that provides a command-line interface for running Git commands on Windows. While PowerShell is designed for managing Windows systems, Git Bash is specifically tailored for working with Git repositories and provides a more familiar environment for developers who are used to Unix-like systems.

# 4) What’s the difference between Anaconda, conda, and Python?
# The difference between Anaconda, conda, and Python is as follows:
# - Anaconda is a distribution of Python and R programming languages for scientific computing and data science. It includes a collection of pre-installed packages and tools for data analysis, machine learning, and visualization.
# - Conda is a package manager that comes with Anaconda. It allows users to manage and install packages, dependencies, and environments for Python and R. Conda can be used to create isolated environments for different projects, making it easier to manage dependencies and avoid conflicts between packages.
# - Python is a high-level programming language that is widely used for various applications, including web development, data analysis, machine learning, and more. It is the core programming language that Anaconda and conda are built around, providing the foundation for the tools and packages included in the Anaconda distribution.

# 5) What is VS Code? 
# VS Code is a source-code editor developed by Microsoft. It is a lightweight and powerful code editor that supports a wide range of programming languages and features. VS Code provides features such as syntax highlighting, code completion, debugging, and version control integration. It also has a large ecosystem of extensions that allow developers to customize their coding environment and add additional functionality. VS Code is widely used by developers for writing and editing code across various programming languages and frameworks.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# Jupyter Notebook is an open-source web application that allows users to create and share documents that contain live code, equations, visualizations, and narrative text. It is commonly used for data analysis, scientific computing, and machine learning. Jupyter Lab is an extension of Jupyter Notebook that provides a more flexible and interactive user interface. It allows users to work with multiple notebooks, terminals, and file browsers in a single workspace. Jupyter Lab also offers additional features such as drag-and-drop functionality, support for multiple file formats, and a more customizable interface compared to Jupyter Notebook.

# 7) What does ~/ mean?
# The symbol ~/ is a shorthand notation that represents the home directory of the current user in a Unix-like operating system. It is used in file paths to indicate that the path starts from the user's home directory. For example, if a user's home directory is /home/username, then ~/documents would refer to /home/username/documents. This notation allows users to quickly navigate to their home directory without needing to specify the full path.

# 8) What’s the difference between an absolute path and a relative path?
# An absolute path is a file path that specifies the complete location of a file or directory from the root directory. It starts with a slash (/) and includes all the directories leading to the file. For example, /home/username/documents/file.txt is an absolute path.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Absolute path: /home/username/course_assignments/homework2
# Relative path: course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# The command to move from "course_assignments/homework2/" to "course_assignments/" is:

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# The command rm ./ would attempt to remove the current directory (./) and all of its contents. However, since rm is a command used to delete files and directories, it would not be able to remove the current directory itself. Instead, it would likely return an error message indicating that it cannot remove the current directory. It is important to be cautious when using the rm command, as it can permanently delete files and directories if used incorrectly.

# 12) What do the following commands do?
# git add
# Git add is a command used to stage changes in the working directory for the next commit. It allows you to specify which files or changes you want to include in the commit. For example, git add <file> will stage a specific file, while git add . will stage all changes in the current directory.

# git commit
# Git commit is a command used to save the staged changes to the local repository. It creates a new commit with a message describing the changes that were made. For example, git commit -m "Added new feature" will create a commit with the message "Added new feature".

# git push
# Git push is a command used to upload local commits to a remote repository. It allows you to share your changes with others and update the remote repository with your latest commits. For example, git push origin main will push the commits from the local main branch to the remote repository named origin.

# 13) What's the difference between "git add ." and "git add <file>"?
# The difference between "git add ." and "git add <file>" is as follows: 
# - "git add ." stages all changes in the current directory and its subdirectories for the next commit. It will include all modified, new, and deleted files in the staging area.
# - "git add <file>" stages a specific file for the next commit. It allows you to choose which changes you want to include in the commit by specifying the file name. For example, git add myfile.txt will stage only the changes made to myfile.txt, while leaving other changes in the directory unstaged. This gives you more control over which changes are included in your commit.

# 14) What do "git status" and "git log -1" do?
# Git status is a command that shows the current state of the working directory and the staging area. It displays which files have been modified, which files are staged for the next commit, and which files are untracked. It also provides information about the branch you are on and any changes that have been made since the last commit.
# Git log -1 is a command that shows the most recent commit in the Git repository. It displays information about the commit, such as the commit hash, author, date, and commit message. The -1 flag limits the output to only the most recent commit, allowing you to quickly see the latest changes made to the repository.

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning a repository is the process of creating a local copy of a remote Git repository. When you clone a repository, you download all the files, commit history, and branches from the remote repository to your local machine. This allows you to work on the code locally and make changes without affecting the original repository until you push your changes back to the remote.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# One of the most frustrating bugs I encountered in this class was when I accidentally deleted a file from my local repository using the rm command. I realized that I had made a mistake and needed to recover the file. To troubleshoot and fix the issue, I first checked if the file was still present in the remote repository by using git status and git log commands. I then used git checkout to restore the deleted file from the last commit. This allowed me to recover the file and continue working on my project without losing any important data. It was a valuable learning experience that taught me to be more cautious when using commands that can modify or delete files in Git.

# 17) What’s a question you still have? What’s something you’re confused about?
# One question I still have is about how to effectively manage and resolve merge conflicts in Git. I understand that merge conflicts can occur when multiple people are working on the same codebase and make conflicting changes to the same file. However, I am still unsure about the best practices for resolving these conflicts and ensuring that the code remains functional after the merge. I would like to learn more about strategies for handling merge conflicts and how to use Git tools to assist in the resolution process.

# 18) Tell me a fun fact!
# My fun fact is that I have broken my nose 7 times throughout my life. It has become somewhat of a running joke among my friends and family. 

# 19) Print your favorite math expression you've learned in Python so far. 
# My favorite math expression I've learned in Python so far is the quadratic formula, which is used to find the roots of a quadratic equation. 
# The formula is given by: 
# x = (-b ± √(b² - 4ac)) / (2a)
# This formula allows us to solve for x when we have a quadratic equation of the form ax² + bx + c = 0. It is a fundamental tool in algebra and has many applications in various fields of science and engineering. I find it fascinating how this formula can provide solutions to a wide range of problems involving quadratic equations.

# (Hint: Use print() and add a comment explaining what it does.)
# This expression calculates the roots of a quadratic equation using the quadratic formula.

import math

a = 1
b = -3
c = 2

discriminant = b**2 - 4*a*c

root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)

print("The roots of the quadratic equation are:", root1, "and", root2)


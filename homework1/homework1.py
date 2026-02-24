# File: homework1.py

# --- Variables and Data Types ---

a = 10
print (a)
print (type(a)) # a is an integer, a whole number with no decimals 

b = 1.5
print (b)
print (type(b)) # b is a float, a number with no decimals

c = 3j
print (c)
print (type(c)) # c is a complex number, a number with a real and imaginary 

d = "hello"
print (d)
print (type(d)) # d is a string, a sequence of characters

e = [1, 2, 3]
print (e)
print (type(e)) # e is a list, a collection of items that are ordered and changeable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print (type(f)) # f is a dictionary, a collection of key-value pairs that are unordered, changeable, and indexed

g = (1, 2)
print (g)
print (type(g)) # g is a tuple, a collection of items that are ordered and unchangeable 

h = ["apple", "banana", "strawberry"]
print (h)
print (type(h)) # h is a list, a collection of items that are ordered and changeable 

i = True
print (i)
print (type(i)) # i is a boolean, a data type that can only be True or False 

j = None
print (j)
print (type(j)) # j is NoneType, a data type that represents the absence of a value or a null value

k = [True, "blue", 12]
print (k)
print (type(k)) # k is a list, a collection of items that are ordered and changeable, and can contain different data types 

l = str(14)
print (l)
print (type(l)) # l is a string, a sequence of characters, and is created by converting the integer 14 to a string using the str() function 

m = 1e4
print (m)
print (type(m)) # m is a float, a number with decimals that is created by using scientific notation (1e4 means 1 * 10^4)



# 1. How many different data types did you find?
# I found 9 different data types.

# 2. List all the data types you found. 
# integer, float, complex, string, list, dictionary, tuple, boolean, and NoneType.

#3. What variables have the same data types?
# e and h and k are all lists
# b and m are both floats
# d and l are both strings. 

#4. What was the data type of l? Why is it not an integer? What does str() do?
# The data type of l is str (string).
# It is not an integer because str(14) converts the number 14 into the text "14". 
# The str() function converts a value into a string. 

#5. Look up one more data type not given above. Repeat the same procedure.

n = {1, 2, 3}
print(n)
print(type(n))  

# n is a set, an unordered collection of unique values
# One additional data type is set, which I added to the code above as variable n.
# A set is an unordered collection of unique values.


# --- Booleans ---

print (10 > 9) # True, 10 is greater than 9

print (10 == 9) # False, 10 is not equal to 9 

print (10 <= 9) # False, 10 is not less than or equal to 9 

bool("abc") # True, non-empty strings are considered True

bool(True) # True, the boolean value True is considered True

bool(0) # False, the integer 0 is considered False 

bool("") # False, an empty string is considered False

bool(" ") # True, a string with a space is considered True

bool(()) # False, an empty tuple is considered False

bool([]) # False, an empty list is considered False 

bool({}) # False, an empty dictionary is considered False 

bool(True and False) # False, because both conditions must be True for the result to be True

bool(True or True) # True, because at least one condition is True for the result to be True

bool(False and False) # False, because both conditions must be True for the result to be True 

bool(True or False) # True, because at least one condition is True for the result to be True 

bool(False or False) # False, because at least one condition must be True for the result to be True

bool(not(False)) # True, because not False is True

bool(not(True)) # False, because not True is False 

#1. What pattern do you notice about expressions returning True or False?
# Expressions that involve comparisons (like >, ==, <=) return True or False based on the relationship between the values being compared. 

#2. Which expression surprised you about its result?
# The expression bool(" ") surprised me because I thought an empty string would be False, but a string with a space is considered True. 

#3. Create an expression, not given above, that will return True. Why is it True?
print (5 < 10) # This expression will return True because 5 is less than 10.

#4. Create an expression, not given above, that will return False. Why is it False?
print (5 > 10) # This expression will return False because 5 is not greater than 10. 


# --- Operators ---

print(10 + 5) # 15, + performs addition 

print (10 - 5) # 5, - performs subtraction

print (2 * 4) # 8, * performs multiplication 

print (6 / 3) # 2 / performs division 

print (5 % 2) # 1, % performs modulus (returns the remainder of the division) 

print (3 ** 2) # 9, ** performs exponentiation (raises the first number to the power of the second number)

print (15 // 2) # 7, // performs floor division (returns the quotient of the division, rounded down to the nearest whole number)

print (5 == 2) # False, == checks if the values on either side are equal 

print (10 != 10) # False, != checks if the value on the left is not equal to the value on the right 

print (2<5) # True, < checks if the value on the left is less than the value on the right 

print (12>5) # True, > checks if the value on the left is greater than the value on the right

print (5 <= 6) # True, <= checks if the value on the left is less than or equal to the value on the right 

print (1 >=10) # False, >= checks if the value on the left is greater than or equal to the value on the right 

x = 5
print (x) # 5, x is assigned the value of 5

x += 5
print (x) # 10, x is now assigned the value of x + 5, which is 5 + 5 = 10

x *= 3
print (x) # 30, x is now assigned the value of x * 3, which is 10 * 3 = 30 

#1. What does the operator and do? Write an expression that results in True. Write an expression that results in False.
# The operator "and" returns True only if both conditions are True. Otherwise, it returns False.
print (5 > 2 and 10 > 3) # True, both conditions are True 
print (3 > 10 and 5 > 2) # False, one condition is False but the other is True 

#2. What does the operator or do? Write an expression that results in True. Write an expression that results in False.
# The operator "or" returns True if at least one condition is True. It only returns False if both conditions are False.
print (5 > 2 or 10 > 3) # True, both conditions are True 
print (3 > 10 or 5 > 2) # True, one condition is False but the other is True 

#3. What does the operator not do? Write an expression that results in True. Write an expression that results in False. 
# The operator "not" negates the value of a boolean expression. If the expression is True, "not" will make it False, and if the expression is False, "not" will make it True.
print (not (5 > 10)) # True, because 5 > 10 is False, and not False is True
print (not (5 > 2)) # False, because 5 > 2 is True, and not True is False

#1. What is the difference between the / and //?
# The / operator performs regular division and returns a float, while the // operator performs floor division and returns an integer (the quotient rounded down to the nearest whole number). 

#2. What is the difference between the % and //?
# The % operator returns the remainder of the division, while the // operator returns the quotient of the division rounded down to the nearest whole number.

#3. What operator would you use to calculate the remainder when dividing two numbers? Give an example. 
# I would use the % operator to calculate the remainder when dividing two numbers. 

#4. How do assignment operators work?
# Assignment operators are used to assign values to variables. They can also be combined with other operators to perform an operation and assignment in one step. 


# --- Strings ---

my_string = "hello"
print (my_string) # Prints: hello

my_string[0]
print (my_string[0]) # Prints: h, the first character of the string

my_string[1]
print (my_string[1]) # Prints: e, the second character of the string

my_string[2]
print (my_string[2]) # Prints: l, the third character of the string

my_string[3]
print (my_string[3]) # Prints: l, the fourth character of the string

my_string[4]
print (my_string[4]) # Prints: o, the fifth character of the string

my_string[-1]
print (my_string[-1]) # Prints: o, the last character of the string

my_string[1:3]
print (my_string[1:3]) # Prints: el, the characters from index 1 to index 2 (3 is not included)

my_string[0:5:2]
print (my_string[0:5:2]) # Prints: hlo, the characters from index 0 to index 4 (5 is not included) with a step of 2 (every second character)

len(my_string)
print (len(my_string)) # Prints: 5, the length of the string (number of characters)

len(my_string + "goodbye")
print (len(my_string + "goodbye")) # Prints: 12, the length of the concatenated string "hellogoodbye" (5 characters from my_string and 7 characters from "goodbye")

len(my_string * 3)
print (len(my_string * 3)) # Prints: 15, the length of the repeated string "hellohellohello" (5 characters from my_string repeated 3 times)


#1. Define the term slicing. For which of the manipulations did you slice your string?
# Slicing is a technique used to extract a portion of a string (or other sequence types) by specifying a range of indices. 
# It allows you to create a new string that is a subset of the original string.
# I sliced my string in the manipulations where I used the syntax my_string[start:stop] or my_string[start:stop:step]. 
# Specifically, I sliced the string in the following manipulations: my_string[1:3], my_string[0:5:2].

#2. Call the following, describe the result:

name = "Oski"
print("Hello, my name is", name)

# The result is: Hello, my name is Oski
# This is a string concatenation where the string "Hello, my name is" is combined with the variable name, which contains the string "Oski". 
# The print function outputs the combined string to the console.

#3. all the following, describe the result.

name = "Oski"
print(f"Hello, my name is {name}")

# The result is: Hello, my name is Oski
# This is an example of an f-string, which allows for string interpolation.
# The expression inside the curly braces {name} is evaluated and replaced with the value of the variable name, which is "Oski". 
# The print function outputs the resulting string to the console.

#4. What is the difference between the two last print statements?
# The difference between the two last print statements is that the first one uses string concatenation with a comma to combine the string and the variable, while the second one uses an f-string for string interpolation.
# In the first print statement, the comma automatically adds a space between the string and the variable when printing. In the second print statement, the f-string allows for more complex expressions and formatting options within the string, and does not automatically add a space unless specified.


# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists the contents of the current directory. Use it to see what files and folders are in the current directory.
# Example: ls 

# ls -a
# Lists all the contents of the current directory, including hidden files. Use it to see all files and folders, including those that are hidden.
# Example: ls -a

# mkdir
# Makes a new directory. Use it to create a new folder.
# Example: mkdir homework1

# cat 
# Concatenates and displays the contents of a file. Use it to view the contents of a file in the terminal.
# Example: cat homework1.py

# pwd
# Prints the current working directory. Use it to see the full path of the current directory you are in.
# Example: pwd

# cd ..
# Moves up one directory level. Use it to go back to the parent directory.
# Example: cd ..

# cd ~
# Moves to the home directory. Use it to quickly navigate to your home directory.
# Example: cd ~

# cp
# Copies a file or directory. Use it to create a copy of a file or folder.
# Example: cp homework1.py homework1_copy.py

# mv
# Moves a file or directory. Use it to move a file or folder to a different location or to rename it.
# Example: mv homework1.py homework1_renamed.py

# rm
# Removes a file or directory. Use it to delete a file or folder.
# Example: rm homework1_copy.py

# clear
# Clears the terminal screen. Use it to remove all previous commands and outputs from the terminal view.
# Example: clear

# grep
# Searches for a specific pattern in a file or input. Use it to find lines in a file that match a certain pattern.
# Example: grep "import" homework1.py (this will search for the word "import" in the file homework1.py and display the matching lines)

#1. Look up 3 other commands not present. Define and explain how to use them on the command line.

# a. touch
# The touch command is used to create a new empty file or to update the timestamp of an existing file.
# Example: touch newfile.txt (this will create a new empty file named newfile.txt in the current directory)

# b. rmdir
# The rmdir command is used to remove an empty directory. It will not work if the directory contains files or other directories.
# Example: rmdir oldfolder (this will remove the directory named oldfolder if it is empty)

# c. head
# The head command is used to display the first few lines of a file. By default, it shows the first 10 lines, but you can specify a different number of lines with the -n option.
# Example: head -n 5 homework1.py (this will display the first 5 lines of the file homework1.py)

#2. What command would you use to create a new file? To delete a file? To see the contents of a file?
# To create a new file, I would use the touch command.
# Example: touch newfile.txt
# To delete a file, I would use the rm command.
# Example: rm newfile.txt
# To see the contents of a file, I would use the cat command.
# Example: cat homework1.py

#3. What is a hidden file?
# A hidden file is a file that is not normally visible when listing the contents of a directory. 
# In Unix-like operating systems, hidden files typically have names that start with a dot (.) and are not displayed by default when using the ls command. 
# Hidden files are often used to store configuration settings or other data that should not be modified by the user.

#4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.

# a. -l (long listing format)
# The -l flag is used with the ls command to display a detailed list of files and directories, including permissions, number of links, owner, group, size, and modification date.
# Example: ls -l (this will display a long listing of the contents of the current directory)

# b. -r (reverse order)
# The -r flag is used with the ls command to reverse the order of the output.
# Example: ls -r (this will display the contents of the current directory in reverse order)

# c. -h (human-readable)
# The -h flag is used with the ls command to display file sizes in a human-readable format (e.g., KB, MB, GB).
# Example: ls -lh (this will display a long listing of the contents of the current directory with file sizes in a human-readable format)



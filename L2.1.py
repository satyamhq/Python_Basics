# -------------------------------
# Strings in Python
# -------------------------------

# A string is a sequence of characters.

# Different ways to define strings
str1 = 'Hello World'      # single quotes
str2 = "Hello World"      # double quotes
str3 = '''Hello World'''  # triple quotes (can be multi-line too)

# -------------------------------
# Escape Sequences
# -------------------------------
# \n = new line, \t = tab, \" = double quote, \\ = backslash

print("Hello World. I am Satyam Kumar")
print("Hello World.\nI am Satyam Kumar")  # new line
print("Hello World.\tI am Satyam Kumar")  # tab space

# -------------------------------
# Basic Operations
# -------------------------------

# 1. Concatenation (joining strings)
print("Hello" + "World")        # HelloWorld
print("Hello" + " " + "World")  # Hello World

# 2. Length of a string
str1 = "Satyam"
str2 = "Kumar"

print(len(str1))   # 6
print(len(str2))   # 5

# Joining with a space
final_str = str1 + " " + str2
print(final_str)           # Satyam Kumar
print(len(final_str))      # 12 (6 + 1 + 5)

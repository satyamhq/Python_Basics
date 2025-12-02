# String Functions

str = "i am Coder and I am Learning Python"

# endswith() → check ending
print(str.endswith("hon"))    # True
print(str.endswith("code"))   # False

# capitalize() → first letter capital
print(str.capitalize())
print(str)

# replace() → replace old with new
print(str.replace("o", "a"))
print(str.replace("Python", "Javascript"))

# find() → first index of substring
print(str.find("o"))    # 6
print(str.find("a"))    # 2

# count() → count occurrence
print(str.count("am"))  # 2
print(str.count("i"))   # 2

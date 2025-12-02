# Slicing
# Definition: Slicing means accessing a part (substring) of a string.
# Syntax: string[start : end]   # end index is not included

str = "Satyam Kumar"

print(str[0:5])          # Satya
print(str[1:4])          # aty
print(str[0:len(str)])   # Satyam Kumar
print(str[:4])           # same as [0:4] → Satya
print(str[5:])           # same as [5:len(str)] → m Kumar

# Negative Index
str = "Apple"
print(str[-3:-1])        # pl

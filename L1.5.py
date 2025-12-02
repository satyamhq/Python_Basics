# ------------------------------------------------------
# Python Notes: String Formatting
# ------------------------------------------------------

name = "Satyam"
age = 18

# 1. Using commas (,) → Auto adds spaces
print("My name is", name, "and I am", age, "years old.")
# Output: My name is Satyam and I am 18 years old

# ------------------------------------------------------

# 2. Using + → Manual join, convert numbers with str()
print("My name is " + name + ". I am " + str(age) + " years old.")
# Output: My name is Satyam. I am 18 years old.

# ------------------------------------------------------

# 3. Using f-strings (Best ✅)
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Satyam and I am 18 years old

print(f"Next year, I will be {age + 1} years old.")
# Output: Next year, I will be 19 years old

# ------------------------------------------------------
# Summary:
# ,   → Quick, adds spaces automatically
# +   → Works, but messy with numbers
# f"" → Clean, flexible, best practice ✅
# ------------------------------------------------------

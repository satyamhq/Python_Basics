# ------------------------------------------------------
# Python Notes: Rules for Identifiers
# ------------------------------------------------------

# An identifier is the name given to variables, functions, classes, etc.

# ✅ Rules for identifiers:

# 1. Identifiers can contain:
#    - Letters (A–Z, a–z)
#    - Digits (0–9)
#    - Underscore (_)

# 2. Identifiers cannot start with a digit.
#    Example: 1name ❌   name1 ✅

# 3. Identifiers cannot contain special symbols.
#    Example: name$ ❌   first_name ✅

# 4. Identifiers cannot be Python keywords.
#    Example: if = 5 ❌   my_if = 5 ✅
#    (keywords are reserved words like if, else, while, for, class, etc.)

# 5. Identifiers are case-sensitive.
#    Example: Name, name, and NAME are three different identifiers.

# 6. Length of an identifier:
# - No strict limit, but use meaningful names
# Example:
#   x          → ❌ not meaningful
#   student_age → ✅ meaningful and clear

# ------------------------------------------------------
# Examples
studentName = "Satyam"     # valid
student_age = 18           # valid
_age = 20                  # valid
name1 = "Python"           # valid

# 1student = "Hello"       # invalid (starts with digit)
# student-name = "Hi"      # invalid (special character '-')
# if = 5                   # invalid (keyword)

# Note :
# All variables are identifiers.
# But not all identifiers are variables (they can also be functions, classes, etc.).

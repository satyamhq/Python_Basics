"""
# Conditional Statement
# if-elif-else (SYNTAX)

if (condition):
    statement1
elif (condition):
    statement2
else:
    statement3
"""

#--------------------------------------------
# Example 1: Voting eligibility
age = int(input("Enter your age : "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")

#--------------------------------------------
# Example 2: Multiple statements inside if
age = 21
if age >= 18:
    print("Eligible for vote")
    print("Eligible for drive")   # Both run if condition is True

#--------------------------------------------
# Example 3: Traffic light system
light = "Green"
if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Look")
elif light == "Red":
    print("Stop")
else:
    print("Light is not working")

#--------------------------------------------
# Example 4: Two independent if statements
num = 5
if num > 2:
    print("Number is greater than 2")
if num > 3:        # This is checked separately
    print("Number is greater than 3")

#--------------------------------------------
# Example 5: if-elif chain (only one block runs)
num = 5
if num > 2:
    print("Number is greater than 2")
elif num > 3:      # This will NOT run because first if was True
    print("Number is greater than 3")

#--------------------------------------------
# Example 6: Grading system
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:       # no need to check <90, already covered
    print("Grade B")
elif marks >= 70:       # no need to check <80, already covered
    print("Grade C")
else:
    print("Grade D")

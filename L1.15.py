#----------------------------------------------------
# Example 1: Traffic Light
light = input("light : ")

if light == "red":
    print("stop")
elif light == "yellow":
    print("look")
elif light == "green":
    print("go")
else:
    print("light is broken")
#----------------------------------------------------

# Example 2: Grading System
marks = int(input("marks : "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("D")
#----------------------------------------------------

# Example 3: Fee Calculation
A = int(input("A : "))
G = input("M/F : ")

if (A == 1 or A == 2) and G == "M":
    print("fee is 100")
elif (A == 3 or A == 4) or G == "F":
    print("fee is 200")
elif A == 5 and G == "M":
    print("fee is 300")
else:
    print("no fee")
#----------------------------------------------------

# Example 4: Voting Eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")
#----------------------------------------------------

# Example 5: Ternary Operator
food = input("food : ")
eat = "Yes" if food == "cake" else "No"
print(eat)
#----------------------------------------------------

# Example 6: Inline if-else
food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")
#----------------------------------------------------

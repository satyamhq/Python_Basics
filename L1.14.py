"""
----------------------------------------------------
Conditional Statements in Python
----------------------------------------------------
- Used to make decisions based on conditions (True/False).

1. if statement
----------------
Syntax:
    if condition:
        statement(s)

Example:
    if age >= 18:
        print("You are an adult")

2. if-else statement
---------------------
Syntax:
    if condition:
        statement(s)
    else:
        statement(s)

Example:
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")

3. if-elif-else statement
--------------------------
Syntax:
    if condition1:
        statement(s)
    elif condition2:
        statement(s)
    elif condition3:
        statement(s)
    else:
        statement(s)

Example:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Fail")

4. Nested if statement
------------------------
Syntax:
    if condition1:
        if condition2:
            statement(s)

Example:
    if age >= 18:
        if citizen == "yes":
            print("Eligible to vote")
        else:
            print("Not eligible to vote")
    else:
        print("Too young to vote")
----------------------------------------------------
"""

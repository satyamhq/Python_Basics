# ----------------------------------------
# Types of Operators in Python
# ----------------------------------------

# 1. Arithmetic Operators
# +   -   *   /   %   //   **
a, b = 10, 3
print(a + b)   # 13   (Addition)
print(a - b)   # 7    (Subtraction)
print(a * b)   # 30   (Multiplication)
print(a / b)   # 3.333... (Division → float)
print(a % b)   # 1    (Modulus → Remainder)
print(a // b)  # 3    (Floor Division)
print(a ** b)  # 1000 (Exponentiation → 10³)

# ----------------------------------------

# 2. Relational / Comparison Operators
# ==   !=   >   <   >=   <=
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False

# ----------------------------------------

# 3. Logical Operators
# Operators: and   or   not

# Example values
x, y = True, False

# AND (both must be True)
print(x and y)   # False → True AND False = False
print(x and x)   # True  → True AND True  = True
print(y and y)   # False → False AND False = False

# OR (at least one must be True)
print(x or y)    # True  → True OR False = True
print(y or y)    # False → False OR False = False
print(x or x)    # True  → True OR True  = True

# NOT (reverses the value)
print(not x)     # False → NOT True  = False
print(not y)     # True  → NOT False = True

# Order
#not > and > or

# ----------------------------------------

# 4. Assignment Operators
# =   +=   -=   *=   /=   %=   //=   **=
num = 5
num += 3    # same as num = num + 3
print(num)  # 8

# ----------------------------------------

# 5. Bitwise Operators
# &   |   ^   ~   <<   >>
p, q = 6, 3   # 6 = 110, 3 = 011 (binary)
print(p & q)   # 2   (AND  → 010)
print(p | q)   # 7   (OR   → 111)
print(p ^ q)   # 5   (XOR  → 101)
print(~p)      # -7  (NOT  → flips bits)
print(p << 1)  # 12  (Left shift)
print(p >> 1)  # 3   (Right shift)

# ----------------------------------------

# 6. Membership Operators
# in   not in
s = "Python"
print("P" in s)       # True
print("z" not in s)   # True

# ----------------------------------------

# 7. Identity Operators
# is   is not
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True   (values are same)
print(a is b)   # False  (different objects in memory)

# ----------------------------------------

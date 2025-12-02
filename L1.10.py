# ----------------------------------------------------
# Expression Execution in Python
# ----------------------------------------------------

# 1. String & Numeric values with *
A, B = 2, 3
Txt = "@"
print(2 * Txt * 3)  
# Output: @@@@@@
# Explanation: 2 * "@" = "@@", then "@@" * 3 = "@@@@@@"

# ----------------------------------------------------
# 2. String & String with + (Concatenation)
A, B = "2", 3
Txt = "@"
print((A + Txt) * B)    
# Step 1: "2" + "@" = "2@"
# Step 2: "2@" * 3 = "2@2@2@"
# Output: 2@2@2@

# ----------------------------------------------------
# 3. Numeric values with arithmetic operators
A, B, C = 2, 3, 4
print(A + B * C)  
# Output: 14
# Explanation: Operator precedence → B*C first, then +A

# ----------------------------------------------------
# 4. Arithmetic expression with int & float → result is float
A, B = 10, 5.0
C = A * B
print(C)  
# Output: 50.0

# ----------------------------------------------------
# 5. Division (/) → always returns float
A, B = 1, 2
C = A / B
print(C)  
# Output: 0.5

# ----------------------------------------------------
# 6. Integer division (//) → floor division
A, B = 1.5, 3
C = A // B
print(C, A / B)  
# Output: 0.0 0.5
# Explanation: // gives floor division (quotient floored).
# If float is involved, result is still float.

# ----------------------------------------------------
# 7. Floor division with positives & negatives
# Rule: A // B = floor(A / B) → closest integer ≤ (A / B)

A, B = 12, 5
print(A // B)   # 2   (12/5 = 2.4 → floor = 2)

A, B = -12, 5
print(A // B)   # -3  (-12/5 = -2.4 → floor = -3)

A, B = 12, -5
print(A // B)   # -3  (12/-5 = -2.4 → floor = -3)

# ----------------------------------------------------
# 8. Modulus (%) → remainder after floor division
# Formula: A % B = A - (A // B) * B
# Note: Remainder has the same sign as denominator (B)

A, B = -5, 2
print(A % B)   # 1   (-5 = (-3 * 2) + 1)

A, B = 5, 2
print(A % B)   # 1   (5 = (2 * 2) + 1)

A, B = -5, -2
print(A % B)   # -1  (-5 = (3 * -2) + -1)

import math

x = input()
x = float(x)
xa = (math.tan(x)) + (1/math.tan(x))                                                          # this is RHS(X) part
ya = (1/math.sin(x)) * (1/math.sin(x)) + (1/math.cos(x))*(1/math.cos(x))
ya = math.sqrt(ya)                                                                          # this is LHS(X) part
if (ya-xa) < 0.001 and xa > 0:                             # checks if RHS(X) is < 0 or not
    print("LHS=RHS so the statement is true ")
else:
    print("x is not in the range where the condition is true as RHS(x) < 0 ")
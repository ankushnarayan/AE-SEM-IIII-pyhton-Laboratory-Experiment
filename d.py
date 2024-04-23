# d) Solve quadratic equation for real numbers.
import cmath

# Prompt the user to input the coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Calculate the roots of the quadratic equation
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

# Check if the roots are real
if sol1.imag == 0:
    sol1 = sol1.real
if sol2.imag == 0:
    sol2 = sol2.real

# Print the roots of the quadratic equation
print("The roots of the quadratic equation are:")
print("Root 1 =", sol1)
print("Root 2 =", sol2)
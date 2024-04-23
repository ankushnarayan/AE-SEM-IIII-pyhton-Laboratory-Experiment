# f) Find the Factorial of a Number
# Prompt the user to input a number
num = int(input("Enter a number: "))

# Find the factorial of the number
fact = 1
for i in range(1, num+1):
    fact *= i

# Print the factorial of the number
print("The factorial of", num, "is", fact)
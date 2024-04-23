#d) Display the multiplication Table based on the given input.
# Prompt the user to input a number
num = int(input("Enter a number: "))

# Display the multiplication table based on the given input
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
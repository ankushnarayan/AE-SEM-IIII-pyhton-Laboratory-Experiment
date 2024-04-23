 # e) Print the Fibonacci sequence.
 # Prompt the user to input the number of terms
n = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
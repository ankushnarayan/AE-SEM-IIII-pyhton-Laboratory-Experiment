# c) Print all Prime Numbers in an Interval.
# Prompt the user to input the start and end of the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Print all prime numbers in the interval
for num in range(start, end+1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

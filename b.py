 # b) Check whether the given year is a Leap Year.
 # Prompt the user to input a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("The year is a leap year.")
        else:
            print("The year is not a leap year.")
    else:
        print("The year is a leap year.")
else:
    print("The year is not a leap year.")
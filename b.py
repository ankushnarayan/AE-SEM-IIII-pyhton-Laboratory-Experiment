   # (b)  Calculate the Area of a Triangle where its three sides a, b, c are given. s=(a+b+c)/2, Area=square root of s(s-a)(s-b)(s-c) (write program without using function)
# Prompt the user to input the lengths of the three sides of a triangle as floats.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the semi-perimeter of the triangle.
s = (a + b + c) / 2

# Calculate the area of the triangle using Heron's formula.
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the calculated area of the triangle.
print("The area of the triangle is {:.2f}".format(area))   
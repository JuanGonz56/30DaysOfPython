import math 

"""
age = 23
height = 75.5 
complex_num = 2 + 3j 

# area of a triangle '''
tri_height = float(input("Enter triangle height: "))
tri_base = float(input("Enter triangle base: "))
tri_area = 0.5 * tri_base * tri_height

print(f"The area of the triangle is: {tri_area}")

# 5 perimeter of a triangle
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))

print(f"The perimeter if the triangle is {side_a + side_b + side_c}")

# 6 input for area and perimeter
rect_length = float(input('Enter the length of the rectangle: '))
rect_width = float(input('Enter the width of the rectangle: ')) 

area_rect = rect_length * rect_width
perimeter_rect = 2 * (rect_width* rect_length)

print(f"The area is: {area_rect}")
print(f"The perimeter is: {perimeter_rect}")

# 7 radius of circle to calculate area and circumference 
radius_circle = float(input('Radius for circle: '))

area_circ = math.pi * radius_circle ** 2
circumference_circ = 2 * math.pi * radius_circle

print(f"The area is {area_circ}")
print(f"The circumference is {circumference_circ}")

"""
"""


# 8 function to calculate the slope y = mX + b 
def calculate_intercepts(m,b):
    
    slope = m 
    y_intercept = (0,b)

    # calculate x-intercept (where y = 0)
    # y = mx + b
    # 0 = mx + b 
    # -b = mx 
    # -b/m = x

    if m != 0:
        x_val = -b/m 
        x_intercept = (x_val, 0)
    else: 
        x_intercept = "undefined (horizontal line)"
        if b == 0:
            x_intercept = "All real numbers (line is the x-axis)"
    
    return slope, x_intercept, y_intercept

# for input equations y = input(m)x + input(b)

m_val = float(input("Enter the slope (m): "))
b_val = float(input("Enter the y-intercept (b): "))

slope, x_intercept, y_intercept = calculate_intercepts(m_val, b_val)

print(f"Equations: y = {m_val}x + {b_val}")
print(f"Slope (m): {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
p1 = (6,10)
p2 = (2,2)

delta_y = p1[1] - p2[1]
delta_x = p1[0] - p2[0]

slope_nine = delta_y/delta_x

print(slope_nine)

squared_dist = delta_x **2 + delta_y **2

distance = math.sqrt(squared_dist)

print(f"the euclidean value is: {distance}")

"""

# 11 calculate the value of y(y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

def calculate_y(x):
    return x**2 + 6*x + 9

# Test the function with different x values
x_values = [-10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in x_values:
    y = calculate_y(x)
    print(f"when x = {x}, y= {y}")
    if y == 0:
        print(f"The value of x that makes y = 0 is: {x}")

# 12 find the length of 'python' and 'dragon' and make a comparison statement
len_python = len('python')
len_dragon = len('dragon')
print(len_python)  
print(len_dragon)
print(len_dragon > len_python)

# 13 use and operator to check if 'on' is in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14 i hope this course is not full of jargon. Use in operator to check if 'jargon' is in the sentence.
sentence = 'i hope this course is not full of jargon'
print('jargon' in sentence)

# 15 
print('on' in 'python' and 'on' in 'dragon')

# 16 find the length of text python and convert the value to float and convert it to string
len_python = len('python')
print(len_python)
print(float(len_python))
result = str(float(len_python))
print(result)
print(type(result))

# 17 even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def is_even(number):
    return number % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False

# 18 check if floor division of 7 by 3 is equal to the int conversion of 2.7
print(7//3 == int(2.7))  # True

# 19 check if '10' is equal to 10
print('10' == 10) # False
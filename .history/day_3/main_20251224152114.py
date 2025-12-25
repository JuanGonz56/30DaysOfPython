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

area_circ = math.pi ** 2
circumference_circ = 2 * math.pi * radius_circle

print(f"The area is {area_circ}")
print(f"The circumference is {circumference_circ}")

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

m_val = 8
b_val = 2

slope, x_intercept, y_intercept = calculate_intercepts(m_val, b_val)

print(f"Equations: y = {m_val}x + {b_val}")
print(f"Slope (m): {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

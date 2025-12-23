import math 

print('Day 2: 30 Days of python programming')

first_name = 'Juan'
last_name = 'Gonzalez'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'Norway'
age = 32
year = 2025
is_married = False
is_true = True
is_light_on = True

birth_month, fav_color, fav_num = 12, 'Purple', 5.5

print(type(full_name),type(country),type(city),type(age),type(year),type(is_married), type(is_true), type(is_light_on))

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

sum = num_one + num_two
subtract = num_two - num_one
product = num_two * num_one
true_division = num_one / num_two
remainder = num_two % num_one
power = num_one ** num_two
floor_division = num_one // num_two

#radius
radius = input("radius: ")
# area of circle pi*R^2
area_of_circle = math.pi * radius * pow(2)

# circumference = 2 * math.pi * radius 
circumference = 2 * math.pi * radius 

print(circumference)

print(f"Sum :{sum} Subtraction :{subtract} Product : {product} True-Div : {true_division} Modulus : {remainder} Floor Div : {floor_division}")
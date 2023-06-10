# Q1 
# Write a function called get_integer that takes a 
# string as its argument, and uses thatstring to prompt 
# the user to enter an integer.
# Your function should return the integersupplied by the user

# prompt = "Could I please have an integer"


# def get_integer(prompt):
#     user_integer = input(prompt)
#     return user_integer

# user_input =  get_integer(prompt)


# print(f"So your integer is {user_input}? Thanks!")

# Q2 Write a function called celcius_convert that takes a 
# number representing thetemperature in Farenheit as its argument, 
# and returns a float representing thetemperature in Celcius

# degrees_f = 350 # Assign some number as the value here

# # Define your function here
# def celcius_convert(degrees_f):
#     degrees_c = float((degrees_f - 32) * 5/9)
#     return degrees_c

# print(celcius_convert(degrees_f))

# Q3 Write a function that accepts one argument (an integer) 
# and returns True when that argument is odd and False when 
# that argument is even. You can use the same formatas the 
# starter code in the previous exercise. Just remember - 
# you're returning the result, not printing it

my_arg = -1

def check_falsiness(my_arg):
    if (my_arg % 2) == 0:
        return False
    else:
        return True

print(check_falsiness(my_arg))

# Q4 
# Write a function that takes two arguments; 
# the unit price of an item, and how manyunits were 
# purchased. Return the total cost as a string

unit_price = 1.49
unit_amount = 7

def calc_cost(unit_price, unit_amount):
    cost = unit_price * unit_amount
    return str(cost)

print(f"The total cost is ${calc_cost(unit_price, unit_amount)}")
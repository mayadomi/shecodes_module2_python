
# Create a variable called first_name and assign Maya to it

first_name = "Maya"
last_name = "Dominice"
programming_language = "Python"

# Data Types - Text data, Numerical data
# Text data: string

today = "Tuesday"
# print(today) # function
# print(f"Today is {today}") # f = format {} variable reference
# print(type(today))

# Numerical data types - Integer, Float
# Integer = whole number

parkers_age = 4
print(type(parkers_age))
print(f"Parker is turning {parkers_age+1} soon!") # concatenate

height = 164
print(f"My height is {height/100} in metres")

# Float
weight = 55.7
print(type(weight))
print(f"My weight is {weight*2.1} pounds.")

distance = "5000"
# print(int(distance) + 8)
# print(distance + str(8))

# dog_name = input("What's the dog's name?")
# print(f"Nice to meet you {dog_name}")

year_born = input("What year were you born?")

# Input data stores data as STRING
print(f"You are {2023-int(year_born)} years old.")

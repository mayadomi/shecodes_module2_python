# Q1 The dictionary below represents the cost of individual items in a supermarket.
# Write a program that asks the user how many of each item they would 
# like in turn, and outputs the total cost of their groceries

# groceries = {"Baby Spinach": 2.78,
#             "Hot Chocolate": 3.70,
#             "Crackers": 2.10,
#             "Coffee": 9.00,
#             "Carrots": 0.56,
#             "Oranges": 3.08
#             }

# grocery_total = 0

# for grocery_item in groceries:
#     # print(grocery_item)
#     number_items = float(input(f"How many of {grocery_item} would you like? "))
#     grocery_total = grocery_total + (number_items*groceries[grocery_item])

# print(grocery_total) 


# Q2 In the last lesson, you wrote a program that counted the 
# number of colour names inthe colours_865.csv file (available here).
# Try rewriting this program so that instead of using separate 
# variables to keep track ofthe number of times each colour 
# name appears, it uses a single dictionary instead.
# Here's a dictionary to get you started

# import csv

# csv_filepath = "csvs/colours_865.csv" #"csvs/colours_20_simple.csv"

# colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}

# with open(csv_filepath, mode='r') as colours_data:
#     reader = csv.reader(colours_data)

#     for colour in reader:
#         if "red" in colour[2].lower():
#             colour_counts["red"] = colour_counts["red"] + 1
#         if "green" in colour[2].lower():
#             colour_counts["green"] = colour_counts["green"] + 1
#         if "yellow" in colour[2].lower():
#             colour_counts["yellow"] = colour_counts["yellow"] + 1
#         if "purple" in colour[2].lower():
#             colour_counts["purple"] = colour_counts["purple"] + 1
#         if "blue" in colour[2].lower():
#             colour_counts["blue"] = colour_counts["blue"] + 1
#         if "orange" in colour[2].lower():
#             colour_counts["orange"] = colour_counts["orange"] + 1

# print(colour_counts)
# with open(csv_filepath, mode='r', encoding='utf-8') as colours_data:
#     reader = csv.reader(colours_data)
#
#     for colour in reader:
#         if "red" in colour[2].lower():
#             red = red + 1
#         if "green" in colour[2].lower():
#             green = green + 1
#         if "blue" in colour[2].lower():
#             blue = blue + 1
#         if "yellow" in colour[2].lower():
#             yellow = yellow + 1

# Q3 Read the colour data from colours_20_simple.csv 
# available in the repo linked above)and save the data in a 
# dictionary where each key is a hex code and each value is the
# corresponding English name.

# For example, the entry for the first colour in the dictionary would look like this

# {"#BEBD7F": "Green beige"}


# import csv

# csv_filepath = "csvs/colours_20_simple.csv" 

# colour_lookup = {}

# with open(csv_filepath, mode='r') as colours_data:
#     reader = csv.reader(colours_data)
#     next(reader, None)  # skip the headers
#     for colour in reader:
#         colour_lookup[colour[1]] = colour[2]
# print(colour_lookup)


# Q4 Modify your code from the previous exercise to save both the English 
# name and RGB code in a list as the value for the corresponding hex code.
# Example
# {"#BEBD7F": ['190-189-127', 'Green beige']...

# with open(csv_filepath, mode='r') as colours_data:
#     reader = csv.reader(colours_data)
#     next(reader, None)  # skip the headers
#     for colour in reader:
#         colour_lookup[colour[1]] = [colour[0], colour[2]]
# print(colour_lookup)

# Q5 (Extra Tricky)Modify your code from the previous exercise to save both the
# English name and RGB code in a dictionary as the value for the corresponding hex code.
# Example:

# {"#BEBD7F": {"RGB": "190-189-127", "English": "Green beige"}    ...
import csv

csv_filepath = "csvs/colours_20_simple.csv" 

hex_dictionary = {}
colour_dictionary = {"RGB": "", "English":""}

with open(csv_filepath, mode='r') as colours_data:
    reader = csv.reader(colours_data)
    next(reader, None)  # skip the headers

    for colour in reader:
        colour_dictionary["RGB"] = colour[0]
        colour_dictionary["English"] = colour[2]
        hex_dictionary[colour[1]] =  colour_dictionary #[colour[0], colour[2]]

print(hex_dictionary)


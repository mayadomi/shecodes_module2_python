# Q1 Write a program that reads in colours_20_simple.csv and print each line of the colour
# data one by one as a string. Use spaces to separate the columns insead of commas.

# import csv

# with open("csvs/colours_20_simple.csv", mode='r', encoding='utf-8') as colours_data:
#     reader = csv.reader(colours_data)
#
#     for colour in reader:
#         print(f"{colour[0]} {colour[1]} {colour[2]}")

# Q2 Write a program that reads in colours_20_simple.csv and outputs the colour data in
# order English, Hex then RGB, like so Green beige, Hex: #BEBD7F, RGB: 190-189-127

# import csv
#
# with open("csvs/colours_20_simple.csv", mode='r', encoding='utf-8') as colours_data:
#     reader = csv.reader(colours_data)
#
#     for colour in reader:
#         print(f"{colour[2]} {colour[1]} {colour[0]}")

# # Q3 Write a program that takes a csv file describing colours, and outputs the number of
# # times each of the following colours appears in the English Name:redgreenblueyellow
# # How many of each colour are there in colours_865.csv?

# import csv
#
# csv_filepath = "csvs/colours_865.csv" #"csvs/colours_20_simple.csv"
#
# red = 0
# green = 0
# blue = 0
# yellow = 0
#
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
#
#     print(f" Red: {str(red)} \n Green: {str(green)} \n Blue: {str(blue)} \n Yellow: {str(yellow)}")

    # Red: 51
    # Green: 78
    # Blue: 101
    # Yellow: 34

# Q4 galaxies.csv contains data about 82 different galaxies and their velocities (km/sec).
# Using this data, print a string showing the galaxy with the slowest velocity, and
# another showing the galaxy with the highest velocity.

import csv

csv_filepath = "csvs/galaxies.csv"

with open(csv_filepath, mode='r', encoding='utf-8') as galaxies:
    reader = csv.reader(galaxies)
    galaxy_dict = {}

    for row in reader:
        galaxy_dict[row[0]]



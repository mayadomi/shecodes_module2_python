# While Loops
#Q1 Continuously ask the user to enter a number 
# until they provide a blank input. 
# Output the sum of all the numbers

# number = input("Enter a number: ")
# sum = 0
# while number:
#     sum = sum + int(number)
#     number = input("Enter a number: ")

# print("Your numbers sum to " + str(sum))

# Q2 Ask the user to enter a in integer number. 
# Print all the odd numbers between 0 and
# that number (inclusive). (Its ok not to 
# worry about negative numbers for now, unless
# you really want a challenge.

# number = int(input("Enter a number: "))
# count = 0
# while count <= number:

#     if (count % 2 != 0):
#         print(str(count))
#     elif count == 0:
#         print(str(count))
#     count = count + 1

# Q3 - Guessing game
# Select a number, and save it as variable in code.
# Ask user to enter number and output whether it is 
# greater or less than seledctec number. Keep asking
# until correct number. Then print congrats.

# correct_number = 12 
# print("Guess the random number! ")
# user_guess = int(input("Make a guess "))

# while user_guess != correct_number:
#     if user_guess < correct_number:
#         print("Too low...")
#         user_guess = int(input("Make a guess "))
#     elif user_guess > correct_number:
#         print("Too high....")
#         user_guess = int(input("Make a guess "))

# print("You got it right!")


# while user_guess != correct_number:
#     if user_guess < correct_number:
#         print("Too low...") # can also ask here for input
#     elif user_guess > correct_number:
#         print("Too high....")
#     user_guess = int(input("Make a guess "))


# For Loops

# Q1 Ask the user for a number. Use a for loop to 
# print the times tables for that number,up to ten:

# user_number = int(input("Enter a number: "))

# for i in range(1,11):
#     print(str(user_number) + " * " + str(i) + " = " + str(i*user_number))


# Q2 Ask the user for an integer. Using a for loop, add up every
# number from 0 up to that integer, then print result

# max_number = int(input("Enter a number: "))
# total = 0
# for number in range(0, max_number+1):
#     total +=  number
# print(str(total))

# Q3 Save a list of numbers to a variable in your script, then 
# use a for loop to print sum of all numbers in list

# my_numbers = [3,5,9,1]
# # my_numbers = [-3, -5, 9, 1]
# # my_numbers = []

# sum = 0
# for number in my_numbers:
#     sum += number # sum = sum + number
# print(str(sum))

# Q4 Mambo Code

# lyrics = [["Monica", "in my life"],
#         ["Erica", "by my side"],
#         ["Rita's", "all I need"],
#         ["Tina's", "what I see"],
#         ["Sandra", "in the sun"],
#         ["Mary", "having fun"],
#         ["Jessica", "here I am"]]

# lyrics.append(["you", "makes me your man (ah!)"])

# for lyric in lyrics: # for name, text in lyrics:
#     print(f"A little bit of {lyric[0]} {lyric[1]};")
# print("*trumpet solo*")

# for name, text in lyrics:
#     print(f"A little bit of {name} {text};")
#Extension Exercises

# Q1 

# groceries = [["Baby Spinach", 2.78],
#             ["Hot Chocolate", 3.70],
#             ["BBQ Shapes", 9.00],
#             ["Bread", 2.10],
#             ["Carrots", 0.56],
#             ["Oranges", 3.08]]
# sum = 0
# for item in groceries:
#     quantity = int(input(f"Enter a quantity for {item[0]}: "))
#     sum = sum + quantity*item[1]
# print(f"Thankyou your total is ${sum}")

# Q2 Guessing game improvement

# Select a number, and save it as variable in code.
# Ask user to enter number and output whether it is 
# greater or less than seledctec number. Keep asking
# # until correct number. Then print congrats.
# import random

# number_range = random.randrange(0,30,1)

# correct_number = 12 

# user_go = 'yes'

# while user_go != 'no':
#     print("Guess the random number! ")
#     # user_guess = int(input("Make a guess "))
#     user_guess = random.randrange(0,30,1) 
#     print("Make a guess : " + str(user_guess))
#     while user_guess != correct_number:
#         if user_guess < correct_number:
#             print("Too low...")
#         else:
#             print("Too high....")
#         # user_guess = int(input("Make a guess "))
#         user_guess = random.randrange(0,30,1)
#         print("Make a guess : " + str(user_guess))

#     print("You got it right!")
#     user_go = input("If you would like to stop playing, type 'no'. Otherwise we'll play again: ")







# Loops help us perform a task multiple times
letters = ["a", "b", "c"]

# two types of loop
# While loop
# count = 0
# while 5 > count: # have to ensure there's a false to condition to avoid infinite loop
#     print("Hello")
#     count = count + 1

# name = input("What is your name? ")
# while name != "Ashley":
#     print("I don't know you.")
#     name = input("Well, what's the new name? ")

# For loops
# letters = ['a', 'b', 'c']

# for letter in letters:
#     print(letter)

# for number in range(10): # range function is similar to slice on lists
#     print(number)

students = [["Cindy", "Emily", "Eve"], ["Julie", "Maddy", "Andrea"], ["Jenny", "Sarah", "Yara"]]

for student in students:
    #print(student)
    for student_name in student:
        print(student_name)
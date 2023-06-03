#Sara is a confident rock climber, but sometimes she forgets her helmet. 
#Rei refuses toclimb with Sara unless she's wearing a helmet, because That's Just Sensible.
# Write a program that sets the value for a boolean variable called sara_has_helmet, andthen 
#prints out a string indicating whether or not Rei is down to climb.


# sara_has_helmet = False

# if sara_has_helmet:
#     print("Let's send it!")
# else sara_has_helmet:
#     print("No way, my brain is my moneymaker!")

# Q2
# Rei is a very careful climber, but sometimes she is forgetful. 
# Even if Sara has a helmet,they still can't go climbing unless Rei 
# remembers to bring her rope.Amend the previous program to add a
# check for the rope before you output the result.

# rei_has_rope = False
# sara_has_helmet = False

# if (sara_has_helmet == True) and (rei_has_rope == True):
#     print("Let's send it!")
# elif (sara_has_helmet == False) and (rei_has_rope == True):
#     print("No way, my brain is my moneymaker!")
# elif (rei_has_rope == False) and (sara_has_helmet == True):
#     print("Who's unprepared now, Rei??")
# elif (rei_has_rope == False) and (sara_has_helmet == False):
#     print("I guess let's just go hiking?")

# if sara_has_helmet and rei_has_rope:
#     print("Let's send it!")
# elif not sara_has_helmet and rei_has_rope:
#     print("No way, my brain is my moneymaker!")
# elif not rei_has_rope  and sara_has_helmet:
#     print("Who's unprepared now, Rei??")
# elif not rei_has_rope and not sara_has_helmet:
#     print("I guess let's just go hiking?")

# Q3
# Write a program that implements the algorithm for
#  red light cameras. 
# The programshould print the string "Flash!" if 
# (and only if) a car is 
# detected driving while the lightis red. 
# If the light is green or amber, the program 
# should print "Do nothing.", evenwhen a car is detected.

# Assumes that there is a finite range of light colors

# light_color = "Green"
# car_detected= False

# if light_color == "Red" and car_detected:
#     print("Flash!")
# else:
#     print("Do nothing")


# if light_color can be anything else, add all the elif checks for 

# Q4
# Write a program that asks the user for their height, 
# and determines whether or notthey are tall enough to 
# ride the rollercoaster, which has a height requirement of120cms.

# user_height = float(input("What is your height (in cms)? "))

# if user_height >= 120:
#     print("Hop on!")
# else:
#     print("Sorry, not today!")

# Q6
# Write a program that asks the user to enter their email 
# address and checks whether itis valid or not. For the purpose
#  of this exercise, you can make the assumption that anemail 
# address is valid if it contains a “@” symbol and a “.” symbol.

# user_email = input("What is your email address? ")

# if "@" in user_email and "." in user_email:
#     print("Email valid")
# else:
#     print("Invalid email detected!")

# Q7
# Will this script print anything to the terminal? 
# Have a think first, decide on youranswer, and then 
# try running it to see if your intuition was correct.
# If you get a different result to what you thought, 
# see if you can come up with an explanation, and 
# then check with a mentor

if "False":
    print("A strange game. The only winning move is not to play.")

# will print - false is a string (not empty) and so evaluates to
# true -- correct
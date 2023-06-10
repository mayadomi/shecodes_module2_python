# Function - an activity that is natural to or

# Examples: print(), input(), len()

# Task Separation
# Function definition

# name = input("What is your name? ")
# age = input("What is your age? ")
# if age >= 18:
#     print("Welcome")
# else:
#     print("Under age, cannot enter.")


# def = function creation keyword
# Task Separation - same code, separated:
def ask_user_name():
    name = input("What is your name? ")

def ask_user_age():
    age = input("What is your age? ")
    if age >= 18:
        message = "Welcome"
        print("Welcome")
    else:
        message = "Under age, cannot enter."
        print("Under age, cannot enter.")
    return message # keyword to pop out result and is immediate exit of function - can be anything
    print("test") #doesn't get executed

#print("Hello")
#ask_user_name() # calling of function - functions are 'read' initially but not executed until called.
#print("Hi")


total = 0 # global variable
def add(number1, number2): # takes an input/arguments/parameters/ 'formal parameters'
    result = number1 + number2
    print(total) #can access
    return result

total = 0 # can access
answer = add(2,4) # order matters for arguments / 'actual parameters'
print(answer)
print(result) # can't access here - local variable - it exists only within function, not outside
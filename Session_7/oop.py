class Dog: #class names first letter is upper case by convention (compared to functions)
    # state/attributes
    # name = "Jett"
    # age = 4
    # breed = "pug"

    # methods, or behaviours
    def eat(self):
        self.weight += 0.5
        print("nom nom")

    def talk(self):
        print("bark bark")
    

    # def __init__(self) -> None:
    #     self.name = "Jett"
    #     self.age = 4
    #     self.breed = "pug"

    def __init__(self,dog_name, dog_age, dog_breed, dog_weight) -> None:
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed
        self.weight = dog_weight

    #def __init__(self):
        #print("Hello") # overloading a method - creating something of same name and knows which one to use
    # self argument, points to object instance itself - refers to itself.

# dog1 = Dog() #instantiate object - dog1 is variable, assigning value that's an instant of dog class

# print(dog1)
# print(type(dog1))
# print(dog1.breed)

# dog1.talk() # don't need to add self in .talk(), hidden in the class
#dog2 = Dog("Max", 5, "jack russel")
#print(dog2.name)

dog3 = Dog("Ninja", 5, "pug", 3)
print(dog3.weight)
dog3.eat()
print(dog3.weight)
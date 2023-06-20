# Q1 Create a class to represent She Codes Students. 
# Attributes that you may want toinclude:
#Name
#Program attended ("Plus" or "Flash")
#Year they attended

# class Students:

#     def __init__(self, name, program, year) -> None:
#         self.name = name
#         self.program = program
#         self.year = year

# Q2Add a __str__ method to your student class that returns a summary 
# of the student'sinformation.For a student named Olivia who attended Plus 
# in 2019, it should look like:"<Student: Olivia, Program: Plus, Year: 2019>"

# class Student:

#     def __init__(self, name, program, year) -> None:
#         self.name = name
#         self.program = program
#         self.year = year
    
#     def __str__(self) -> str:
#         return f"Student: {self.name}, Program: {self.program}, Year: {self.year}"
    

# student1 = Student(name="Olivia", program="Plus", year="2019")
# print(student1)

# Q3 Write a class that represents a rectangle shape and has a method for 
# each of the following:
# Calculating the area.
# Calculating the perimeter.
# Calculating the length of the diagonal.
# Determining whether or not the rectangle is a square.
# Here’s the initialiser method to help get you started:
import math

class Rectangle:

    def __init__(self, width: float, height:float):
        self.width = width
        self.height = height

    def calc_area(self):
        self.area = self.width * self.height
    
    def calc_perimeter(self):
        self.perimeter = 2*(self.width + self.height)
    
    def calc_diagonal(self):
        self.diagonal = math.sqrt((pow(self.width,2) + pow(self.height,2)))
    
    def check_square(self):
        if self.width == self.height:
            self.check = "Square"
        else:
            self.check = "Rectangle"


squarything = Rectangle(6, 6)
squarything.calc_area()
print(squarything.area)
squarything.calc_perimeter()
print(squarything.perimeter)
squarything.calc_diagonal()
print(squarything.diagonal)
squarything.check_square()
print(squarything.check)
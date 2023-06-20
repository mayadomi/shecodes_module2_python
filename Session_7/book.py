class Book: #Book() --> use brackets to inherit from another class 
    def __init__(self, title, author, pages, current_page) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1
    
    def __str__(self): # change how string representation of an object ie when you do print(object)
        return f"Title: {self.title}, Author: {self.author}"
    
    def bookmark_page(self):
        self.bookmark = self.current_page

    def turn_page(self):
        self.current_page += 1
    

myBook = Book("A great novel", "Bee Boop")

print(myBook)
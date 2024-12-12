#Part (i)
class Book():# Class
    def __init__(self, author, pages):
        self.author = author #Attributes
        self.pages = pages# Attributes
    def book_details(self): #Method
        print(f"The author is{self.author} with {self.pages} number of pages.")
Book1 = Book(author="Jovita", pages=44) #Instance
print(Book1.book_details())# Displays the information

#Part (ii)
class EBook(Book):
    def __init__(self, author, pages, format_):#It inherits from Book class 
        super().__init__(author, pages)
        self.format_ = format_ #Addition of the format to the EBook class 
EBook1 = EBook(author='Danie', pages=567, format_="PDF")
EBook1.book_details() #Displays the  information

#Part (iii)
def details_of_a_book(): #The function
    class Book:
      title = "Women In Tech"
      author = "Aisha"
    details = Book()
    print(details.title) #returns book title
    print(details.author) #Returns its authors
details_of_a_book()

#Part (iv)
# A class is a blue print that has an instance created by an object.
#Class consist of attributes 

#An object is like a feature that is told what to do by the class with use of the attributes.



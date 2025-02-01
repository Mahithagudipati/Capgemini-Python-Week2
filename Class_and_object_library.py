# •	3. You are building a Library Management System. Create a `Book` 
# class with properties like `title`, `author`, and `isbn`. Write a method to display book details.

class Library:
    def book(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"The title of the book is : {self.title}\n  The author of the book is : {self.author}\n The Isbn number of the book is : {self.isbn}")

l=Library()
l.book("Harry Potter","J.K.Rowling",1234)
l.display()
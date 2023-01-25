class Book:

    def __init__(self,title,author,pages):

        print("A boos is created")

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return "Title:{0} , author:{1}, pages:{2} ".format(
            self.title, self.author, self.pages)

    def __len__(self):

        return self.pages

    def __del__(self):

        print("A book is destroyed")

book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print(book)
print(len(book))
del book
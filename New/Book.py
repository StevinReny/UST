
class Book:
    def __init__(self,book_id:int,title:str,author:str):
        self.book_id=book_id
        self.author=author
        self.title=title


    def display(self):
        print(f"The book id is {self.book_id} name is {self.title} written by {self.author}")




from New.Library import Library

class User:
    def __init__(self,userid,name):
        self.userid=userid
        self.name=name

    def display(self):
        print(f"The user id is {self.userid}{self.name}")


class LibraryUser(User):
    user_books = []
    borrowed_books=[]#storing bookid

    def __init__(self,userid:int,name:str):
        super().__init__(userid,name)




    def borrow(self, bookid:int):
        if bookid not in self.borrowed_books and bookid in Library.booklist:
            self.user_books.append([self.userid, bookid])
            self.borrowed_books.append(bookid)
            print(f"The {self.userid} borrowed {Library.booklist[bookid][0]}")
        else:
            print("The book is not available")

    def returnn(self,bookid:int,userid:int):
        test1=[userid,bookid]
        if bookid in self.borrowed_books and test1 in self.user_books:
            self.borrowed_books.remove(bookid)
            print(f"The {Library.booklist[bookid][0]} is returned")
        else:
            print("Enter the valid bookid")


    def trackuser(self,userid:int):
        lst=[]
        for book in self.user_books:
            if book[0]==userid:
                lst.append(book[1])
        print(f"The userid borrowed {lst} books")


#
# def main():
#     lb = Library()
#
#     lb.addbook(1, "macbeth", "dd")
#     lb.addbook(2, "Merchant of venice", "ddd")
#     lb.addbook(3, "Thankapan", "ddd")
#     lb.addbook(4, "panmac of venice", "ddd")
#     lu=LibraryUser(101,"sh")
#     lu.display()
#     lu.borrow(1,101)
#     lu.borrow(2,101)
#     lu.borrow(2,101)
#     lu.returnn(5,101)
#     lu.returnn(2,101)
#     lu.trackuser(101)
#
# if __name__=="__main__":
#     main()


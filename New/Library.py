import operator
import re

from New.Book import Book


class Library:

    booklist={}
    def __init__(self):
        pass

    def describe(self):
        print(self.booklist)
        # for key,value in self.booklist.items():
        #     print((key,value))


    def addbook(self,book_id:int,title:str,author:str):
        a=Book(book_id,title,author)
        if book_id in self.booklist.keys():
            print("BookId already present")
        else:
            self.booklist[a.book_id]=[a.title,a.author]
            print(f"{book_id}is added to Library" )

    def removebook(self,bookid:int):
        count=0
        if bookid in self.booklist:
            count=1
            del self.booklist[bookid]
        if count==1:
            print("Successfully removed")
        else:
            print("Not found")

    def search(self,name:str):
        lst=[]
        for book in self.booklist:
            if name in self.booklist[book][0]:
                lst.append([book,self.booklist[book][0]])

            # if operator.contains(book.title,name):
            #     print("yes")
            # if re.search(name,book.title):
            #     print("yes")
            # if book.title.find(name)!=-1:
            #     print("yes")
            # if name in book.title:
            #     lst.append([book.book_id,book.title])
        if len(lst)!=0:
            print(lst)
        else:
            print("Not found")

#
# def main():
#     lb=Library()
#
#     lb.addbook(1,"macbeth","dd")
#     lb.addbook(2,"Merchant of venice","ddd")
#     lb.addbook(3,"Thankapan","ddd")
#     lb.addbook(4,"panmac of venice","ddd")
#     lb.removebook(2)
#     # lb.describe()
#     # lb.search("mac")
#
#
# if __name__=="__main__":
#     main()
import traceback

from New.Library import Library
from New.User import LibraryUser

def main():

    while True:
        print("1.Add books to Library\n2.Add user \n3. Remove book\n4.Search book\n5.Show all books\n6.Exit")
        try:
            choice=int(input("Enter the choice"))
            if choice==1:
                id=int(input("Enter the book id").strip())
                title=input("Enter the title").lower().strip()
                author=input("Enter the author").lower().strip()
                lb=Library()
                lb.addbook(id,title,author)
            elif choice==2:
                userid=int(input("Enter the user id").strip())
                name=input("Enter the name").lower().strip()
                lb=LibraryUser(userid,name)
                print("1. Borrow 2.Return 3.Track 4.Display user")
                choice1=int(input("Enter the choice").strip())
                if choice1==1:
                    bookid = int(input("Enter the bookid").strip())
                    lb.borrow(bookid)
                elif choice1==2:
                    bookid = int(input("Enter the bookid").strip())
                    lb.returnn(bookid, userid)
                elif choice1==3:
                    lb.trackuser(userid)
                elif choice1==4:
                    lb.display()
                else:
                    print("Invalid choice")
            elif choice==3:
                bookid = int(input("Enter the book id").strip())
                lb = Library()
                lb.removebook(bookid)
            elif choice==4:
                name=input("Enter the name").lower().strip()
                lb=Library()
                lb.search(name)
            elif choice==5:
                lb=Library()
                lb.describe()
            elif choice==6:
                exit()
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error occurred")
            print(traceback.format_exc(e))
            exit()

if __name__ == "__main__":
    main()





    #
    # lb = Library()
    #
    # lb.addbook(1, "macbeth", "dd")
    # lb.addbook(2, "Merchant of venice", "ddd")
    # lb.addbook(3, "Thankapan", "ddd")
    # lb.addbook(4, "panmac of venice", "ddd")
    # lu=LibraryUser(101,"sh")
    #
    # lu.display()
    # lu.borrow(1)
    # lu.borrow(2)
    # lu.borrow(2)
    # lu.returnn(5)
    # lu.borrow(2)
    # lu.trackuser(101)

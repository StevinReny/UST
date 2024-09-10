import traceback

from Student1.School import School, AdvancedSchool


def main():
    while True:
        try:
            print("1.Add student\n2.Remove student\n3.Search student\n4.Display students\n5.Display student with above grade\n6.Exit")
            choice=int(input("Enter the choice").strip())
            if choice==1:
                sid=int(input("Enter the id ").strip())
                if sid in School.student_list:
                    print("Student id already present")
                else:
                    name=input("Enter the name").strip()
                    sc=School()
                    sc.add(sid,name)
            elif choice==2:
                sid = int(input("Enter the id ").strip())
                sc=School()
                sc.remove(sid)
            elif choice==3:
                sid = int(input("Enter the id ").strip())
                sc = School()
                sc.search(sid)
            elif choice==4:
                sc = School()
                sc.display1()
            elif choice==5:
                if len(School.student_list)==0:
                    print("The Student list is empty")
                else:
                    grade=input("Enter the average").strip()
                    sc = AdvancedSchool()
                    sc.findaboveavg(grade)
            elif choice==6:
                exit()
            else:
                print("Invalid choice")
        except ValueError as e:
            print("error")
        except Exception as e:
            print("Error")
            traceback.format_exc(e)
            exit()

if __name__=="__main__":
    main()
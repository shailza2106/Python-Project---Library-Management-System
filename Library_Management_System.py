class Library:
    def __init__(self,books_present):
        self.books=books_present

    def display_books(self):
        print("*** The books present in th Central Library are ***")
        for index,books in enumerate(self.books):
            print(f"{index+1} -> {books}")

    def assign_books(self,bookname):
        if bookname in self.books:
          self.books.remove(bookname)
          print(f"You have been assigned the book {bookname}. Please keep it safe and return it within a period of 30 days.")
        else:
            print(f"This {bookname} is not present in the Library right now. Please check within a few days.")

    def return_book(self,bookname):
        print(f"The book {bookname} has been added to the Library. Thanks for using our Library Management System.")
        self.books.append(bookname)

class Student:
    
    def basicInfo(self,student_name):
        self.name=student_name
        print(f"{student_name} has borrowed the above book from the Central Library.")
    def timePeriod(self,no_of_days):
        self.no_of_days=no_of_days
        
        if self.no_of_days>30:
            print(f"The total fine is : Rs. {no_of_days-30}")
        else:
            print("The total fine = Rs.0")



if __name__=="__main__":
    centralLibrary=Library(["Computer","Python","R Programming","Statistics","FMS","FAS"])
    studentInfo=Student()
    student_name=input("Please enter your name :")
    print(f"*** Hi {student_name}! Welcome to the Central Library ***")
     print("\t1. Press 1 to display the books name.\n\t2. Press 2 to take a book.\n\t3. Press 3 to return a book.\n\t4. Press 4 to exit the Library.")
    

    while(True):
        user_input=int(input("Please enter your choice: "))
        if user_input==1:
            centralLibrary.display_books()
        elif user_input==2:
            book_name=input("Enter the name of the book you want to borrow: ")
            centralLibrary.assign_books(book_name)
            studentInfo.basicInfo(student_name)
        elif user_input==3:
            book_name=input("Enter the name of the book that you want to return: ")
            no_of_days=int(input("Please enter the total number of days the book was with you : "))
            centralLibrary.return_book(book_name)
            print(f"Thanks for returning the book {book_name} to the Central Library")
            studentInfo.timePeriod(no_of_days)
        else :
            print(f"Thank you {student_name} for using the Central Library. Have a nice day ahead!!")
            break


    
    

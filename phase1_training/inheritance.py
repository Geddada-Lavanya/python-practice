#SINGLE INHERITANCE
# class Student:
#     name="Aravind"
#     def show(self):
#         print(f"Name:{self.name}")
# class marks(Student):
#     def __init__(self,marks):
#         self.marks=marks
#     def show_marks(self):
#         print("marks:",self.marks)
# obj=marks(30)
# print(obj.name)
# obj.show()
# obj.show_marks()    

# --------------------------------------------------------------------
#MULTILEVEL INHERITANCE

# class Student:
#     name="Aravind"
#     def show(self):
#         print(f"Name:{self.name}")
# class marks(Student):
#     def __init__(self,marks):
#         self.marks=marks
#     def show_marks(self):
#         print("marks:",self.marks)
# class staff(marks):
#     def details(self,emp_id,sub):
#         self.emp_id=emp_id
#         self.sub=sub
#         print(f"emp_id:{emp_id},subject:{sub}")
# obj=staff(30)
# print(obj.name)
# obj.details(202,"AIML")
# obj.show()
# obj.show_marks()

# -------------------------0r----------------------------------------------------
# WHEN WE HAVING 2 DEFAULT CONSTRUCTORS IN 2 CLASSES(we use super keyword)


# class Student:
#     name="Aravind"
#     def show(self):
#         print(f"Name:{self.name}")
# class marks(Student):
#     def __init__(self,marks):
#         self.marks=marks
#         super().__init__(name)
#     def show_marks(self):
#         print("marks:",self.marks)
# class staff(marks):
#     def __init__(self,staff_id,marks,name):
#         super().__init__marks(staff_id)
#     def details(self):
#         print(f"staff_id:{self.staff.id}")
# obj=staff(30)
# print(obj.name)
# obj.details(202,"AIML")
# obj.show()
# obj.show_marks()


# --------------------------------------------------------------------------------
#Hierarchial Inheritance

# class clg:
#     name_clg="pragati"
#     adr="ADB road"
#     def clg_det(self):
#         print(self.name_clg,self.adr)
# class student(clg):
#     name="Lavanya"
#     def stu_det(self):
#         print(self.name)
# class staff(clg):
#     staff_id="2002"
#     def staff_det(self):
#         print(self.staff_id)
# obj1=student()
# obj2=staff()
# obj1.clg_det()
# obj2.clg_det()
# obj1.stu_det()
# obj2.staff_det()

# -------------------------------------------------------------------------------------

#multiple Inheritance

# class student:
#     name="Akash"
#     def details(self):
#         print(self.name)
# class staff:
#     staff_id=2002
#     def staff_det(self):
#         print(self.staff_id)
# class clg(student,staff):
#     name_clg="pragati"
#     adr="ADB road"
#     def clg_det(self):
#         print(self.name_clg,self.adr)
# obj=clg()
# obj.staff_det()
# obj.details()

# -------------------------------------------------------------------------------------

# example for encapsulation and inheritance concepts

# class Book:
#     def __init__(self,title,author,avail_copies):
#         self.__title=title
#         self.__author=author
#         self.__avail_copies=avail_copies

#     def borrow_book(self):
#         if self.__avail_copies>0:
#             self.__avail_copies-=1
#             print(f"1 book borrowed {self.__title}")
#         else:
#             print("There are no books available")

#     def return_book(self):
#         self.__avail_copies+=1
         
#     def get_details(self):
#         print(f"Title:{self.__title}\nAuthor:{self.__author}\navailable copies:{self.__avail_copies}")
        
# class Ebook(Book):
#     def __init__(self,file_size,title,author,avail_copies):
#         self.__file_size=file_size
#         super().__init__(title,author,avail_copies)
#         self.title=title
#         self.author=author
        

#     def download(self):
#         print(f"Title:{self.title}\nAuthor:{self.author}\nfile size:{self.__file_size}")

        
# obj=Ebook(200,"python","Lavanya",10)
# obj.borrow_book()
# obj.return_book()
# obj.get_details()
# obj.download()
    
# ---------------------------------------------------------------------------------------------------------------

#example for multiple inheritance

class Book:
    def __init__(self,title,author,avail_copies):
        self.__title=title
        self.__author=author
        self.__avail_copies=avail_copies

    def borrow_book(self):
        if self.__avail_copies>0:
            self.__avail_copies-=1
            print(f"1 book borrowed {self.__title}")
            print(self.__avail_copies)
            return True
        else:
            print("There are no books available")
            return False

    def return_book(self):
        self.__avail_copies+=1
        return "Book returned"
         
    def get_details(self):
        print(f"Title:{self.__title}\nAuthor:{self.__author}\navailable copies:{self.__avail_copies}")

class Member:
    def __init__(self,mem_name,mem_id):
        self.__mem_name=mem_name
        self.__mem_id=mem_id

    def get_mem_details(self):
        print(f"mem_name:{self.__mem_name}\n mem_id:{self.__mem_id}")

    def greet_member(self):
        print(f"Welcome {self.__mem_name}")

class Transaction(Book,Member):
    def __init__(self,mem_name,mem_id,title,author,avail_copies):
        Member.__init__(self,mem_name,mem_id)
        Book.__init__(self,title,author,avail_copies)
        # self.mem_name=mem_name
        # self.mem_id=mem_id                  
        # self.author=author
        # self.title=title
        # self.avail_copies=avail_copies

    def issue_book(self):
        if(self.borrow_book()):
            self.get_mem_details()
        else:
            print("Books Unavailable")

    def return_book_member(self):
        print(self.return_book())

obj=Transaction("Kavya",123,"python","lavanya",200)
obj.greet_member()
obj.borrow_book()
obj.get_details()
obj.issue_book() # In this issue book again having borrow book
obj.return_book_member()
obj.get_details()




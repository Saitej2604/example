"""
Write a program to demonstrate single inheritance where:
 Class Person has attributes name and age.
 Class Student inherits from Person and adds roll number and course.

Class Person has attributes name and age.

"""
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_details(self):
#         print(f'student name: {self.name} \n age: {self.age}')
# class student(person):
#     def __init__(self, cource,roll_no,name,age):
#         super().__init__(name,age)
#         self.cource = cource
#         self.roll_no = roll_no
#     def student_details(self):
#         print(f'student course: {self.cource} \n roll_no: {self.roll_no}')
#         self.person_details()
# p=student('python',22,"saitej",19)
# p.student_details()

# class restrunt:
#     restrunt_name = "pista house"
#     owner = "ramu kaka"
#
#     def restrunt_details(self):
#         print(f"restrunt name : {self.restrunt_name} \n owner : {self.owner}")
#
#
# class loc1(restrunt):
#     def __init__(self, name, manager):
#         self.name = name
#         self.manager = manager
#
#     def loc_details(self):
#         self.restrunt_details()
#         print(f"loc :{self.name} \n manaer : {self.manager}")
#
#
# class loc2(restrunt):
#     def __init__(self, name, manager):
#         self.name = name
#         self.manager = manager
#
#     def loc2_details(self):
#        self.restrunt_details()
#        print(f"loc :{self.name} \n manaer : {self.manager}")
#
#
# r = loc1("uppal", "naveen")
# r1 = loc2("vanastalipuram", "prashanth")
# r.loc_details()
# r1.loc2_details()
#
#
#
"""1. Create a Base Class LibraryItem

Attributes:

title

author

year

Constructor:

Initializes the above 3

Method:

show_details() → prints the above details

🔹 2. Create a Class Book that Inherits from LibraryItem

Extra Attribute:

genre

Constructor:

Use super() to initialize base class attributes

Then initialize genre

Method:

Override show_details() to include genre as well

Add method:

set_genre() → allows method chaining

🔹 3. Create a Class Magazine that Inherits from LibraryItem

Extra Attributes:

issue_number

Constructor:

Use super() to initialize base class attributes

Then initialize issue_number

Method:

Override show_details() to include issue_number

Add method:

set_issue_number() → allows method chaining

🔹 4. Create Objects and Use Method Chaining

Create 1 object of Book, set genre using chaining.

Create 1 object of Magazine, set issue number using chaining.

Call show_details() for both."""

class LibraryItem:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def show_details(self):
        print(F"title : {self.title} \n"
              F"author : {self.author}\n"
              F"year : {self.year}")
class Book(LibraryItem):
    def __init__(self,title,author,year,genre):
        super().__init__(title,author,year)
        self.genre = genre

    def show_details(self):
        super().show_details()
        print(F"genre : {self.genre} \n")
class magazine(LibraryItem):
    def __init__(self,title,author,year,issue_number):
        super().__init__(title,author,year)
        self.issue_number=issue_number
    def issue_number(self):
        print(F"issue number : {self.issue_number} \n")

    def show_details(self):
        super().show_details()
        magazine.issue_number(self)
# b=Book('mybook',"saiteja",2021,"horror")
# b.show_details()
# mag=magazine("mybook","saiteja",2021,"4")
# mag.show_details()
b=Book()
b.show_details("mybook","saiteja",2021,"horror")



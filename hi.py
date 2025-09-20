# class Base:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def display_details(self):
#         print(f"name : {self.name} \n"
#               f"id : {self.id} \n")
# class Student(Base):
#     def __init__(self, name, id,course,marks):
#           super().__init__(name, id)
#           self.course = course
#           self.marks = marks
#     def display_details(self):
#         super().display_details()
#         print(f"course : {self.course} \n"
#               f"marks : {self.marks} \n")
# class Teacher(Base):
#     def __init__(self, name, id,sub,salary):
#         super().__init__(name, id)
#         self.sub = sub
#         self.salary = salary
#     def display_details(self):
#         super().display_details()
#         print(f"sub : {self.sub} \n"
#               f"salary : {self.salary} \n")
# class Staff1(Base):
#     def __init__(self, name, id,department,working_hours):
#         super().__init__(name, id)
#         self.department = department
#         self.working_hours = working_hours
#     def display_details(self):
#         super().display_details()
#         print(f"department : {self.department} \n"
#               f"working_hours : {self.working_hours} \n")
#
# members = [
#         Student("Riya", "S101", "B.Tech", 89),
#         Teacher("Arjun", "T201", "Mathematics", 45000),
#         Staff1("Kavya", "ST301", "Library", 40)
#     ]
#
# for m in members:
#         m.display_details()
#


class Base:
    def __init__(self,brand,model,year):
        self.barnd=brand
        self.model=model
        self.year=year
    def display_info(self):
        print(F"Brand :{self.barnd} \n"
              F" Model :{self.model} \n"
              F" Year :{self.year}")
class Car(Base):
    def __init__(self,brand,model,year,fuel_type,seating_capacity):
        Base.__init__(self,brand,model,year)
        self.fuel_type=fuel_type
        self.seating_capacity=seating_capacity
    def display_info(self):
        print("CAR DETAILS")
        super().display_info()
        print(F"Fuel Type :{self.fuel_type} \n"
              F"Seating Capacity :{self.seating_capacity} \n")
class Bike (Base):
    def __init__(self,brand,model,year,engine_capacity,type):
        Base.__init__(self,brand,model,year)
        self.engine_capacity=engine_capacity
        self.type=type
    def display_info(self):
        print("BIKE DETAILS")
        super().display_info()
        print(F"Engine Capacity :{self.engine_capacity} \n"
              F"Type :{self.type} \n")
class Truck(Base):
    def __init__(self,brand,model,year,load_capacity,wheels):
        Base.__init__(self,brand,model,year)
        self.load_capacity=load_capacity
        self.wheels=wheels
    def display_info(self):
        print("TRUCK DETAILS")
        super().display_info()
        print(F"Load Capacity :{self.load_capacity} \n"
              F"Wheels :{self.wheels} \n")
Members=[

        Car("Toyota", "Camry", 2020, "Petrol", 5),
    Bike("Yamaha", "R15", 2021, "150cc", "Sports"),
    Truck("Tata", "HaulX", 2019, "10000kg", 12)
]
for v in Members:
    v.display_info()

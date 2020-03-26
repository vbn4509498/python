# class Member :
#     def __init__(self,new_gender , new_major , new_id):
#         self.__gender = new_gender  # __ 兩個底線 private
#         self.major = new_major
#         self.id = new_id
#     def set_gender(self, new_gender):
#         if new_gender == "M" or new_gender == "F":
#             self.__gender = new_gender
#         else:
#             print("請傳入'M'或'F'")
#     def get_gender(self):
#          return self.__gender
#     def borrow_resources(self):
#         print("someone borrow")
# class Student(Member):
#     def __init__(self,new_gender , new_major , new_id):
#         super().__init__(new_gender , new_major , new_id)
#     def join_class(self):
#         pass
#     def quit_class(self):
#         pass
#     def borrow_resources(self):
#         print("student borrow")
# class Professor(Member):
#     def __init__(self,new_gender , new_major , new_id):
#         super().__init__(new_gender , new_major , new_id)
#     def borrow_resources(self):
#         print("Professor borrow")
# studentA = Student("M","工管系","B10821031")
# print(studentA.get_gender())
# print(studentA.major)
# print(studentA.id)
# studentA.borrow_resources()
# studentB = Student("B","數媒系","A10821031")
# professorA = Professor("M","財金系","C10821031")
# professorB = Professor("A","企管系","D10821031")
# ls = [studentA,studentB,professorA,professorB]
# for item in ls:
#     item.borrow_resources()
class Pokemon :
    def __int__(self,name,weight,height,food,cp):
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__food = food
        self.__cp = cp
    def eat (self) :
        print(f'The pokemon is eating {self.__food}')
    def make_noice(self):
        print('The pokemon wow wow wow!')
    def set_name(self, new_name):
        self.__name = new_name
    def set_weight(self, new_weight):
        self.__weight = new_weight
    def set_height(self, new_height):
        self.__height = new_height
    def set_food(self, new_food):
        self.__food = new_food
    def set_cp(self, new_cp):
        self.__cp = new_cp
    def get_name(self):
         return self.__name
    def get_weight(self):
         return self.__weight
    def get_height(self):
         return self.__height
    def get_food(self):
         return self.__food
    def get_cp(self):
         return self.__cp
class Pikachu(Pokemon):
    def eat(self):
        print(f'{self.get_name()}is eating {self.get_food()}.Pika')
    def make_noice(self):
        print(f'{self.get_name()}pika pika chu!')
class Squirtle(Pokemon):
    def eat(self):
        print(f'{self.get_name()}is eating{self.get_food()}.jenny jenny!')
    def make_noice(self):
        print(f'{self.get_name()} jenny jenny!')

# pokemon = Pokemon('pokemon',10,10,'堅果',100)
# pikachu =Pikachu('pikachu',20,20,'果實',80)
# ls = [pikachu,pokemon]
# for item in ls :
#     item.make_noice()
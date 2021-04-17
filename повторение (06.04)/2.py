# class Human:
#     def __init__(self,name, lastname, age, 
# place,years):
#         self.__name = name
#         self.__lastname = lastname
#         self.__age = age
#         self.__place = place
#         self.__years = years

#     def show(self, name, lastname, age, place, years):
#         raise NotImplementedError("Класс наследник должен реализовать данный метод")
#         # print("Имя:" + name + "\n", "Фамилия:" + lastname +"\n", "Возраст:" + age + "\n","Место рождения:"+ place +"\n", "Год рождения": + age + "\n")
#         print("имя:", self.lastname,"возраст: ", self.age,"место рождения:", self.place, "год рождения:", self.years)

#     def GetAge(age):
#         return age


# class Student(Sapiens):
#     def __init__(self, name,  lastname, age, place, years):
#         Human.__init__(self, name)
#         Human.__init__(self, lastname)
#         Human.__init__(self, age)
#         Human.__init__(self, place)
#         Human.__init__(self, years)

#     #     self.__age = 1
#     # def speak(self, voice):
#     #     print(self.name, "is saying", voice)

#     @property
#     def age(self):
#         return self.__age
       
 

# class Teacher(Human):
#         def __init__(self, name,  lastname, age, place, years):
#         Teacher.__init__(self, name)
#         Teacher.__init__(self, lastname)
#         Teacher.__init__(self, age)
#         Teacher.__init__(self, place)
#         Teacher.__init__(self, years)






# # dog = Dog("Jerry")
# # dog.speak("gav")
# # dog.show()
 
class Human:
    _age: int = 0
    def __init__(self, firstname, lastname, age, place, years):
        self.firstname, self.lastname, self.age, self.place, self.years
    @property
    def GetAge(self):
        return self._age
    def name(self):
        self.__name
    def lastname(self):
        self.__lastname
    def age(self):
        self.age
    def place(self):
        self.place
    def years(self):
        self.years    
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")


    def show(self):
        print("имя:",self.__firstname, "фамилия:", self.__lastname,"возраст: \t", self.__age,"место рождения:", self.__place, "год рождения:", self.__years)

class Student(Human):
    def details(self, company):
        print(self.firstname, "учится в вузе в компании:", company, "фамилия:", self.__lastname,"возраст: \t", self.age,"место рождения:", self.place, "год рождения:", self.years)


sasha = Student("Саша", "Маршаков", 25, "Иваново", 1961)
sasha.Age = 25
sasha.show()
masha = Teacher("Мария Иванова", "Калашникова", 49,"Москва", 1934)
masha.age = 49
masha.show()
       


    


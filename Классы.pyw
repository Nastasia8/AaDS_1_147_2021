class Human:
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


Ira = Student("Ира", "Ильинцева", 18, "Иваново", 2002)
Ira.Age = 18
Ira.show()
Nata = Teacher("Наталья Викторовна", "Абрамова", 47,"Москва", 1974)
Nata.age = 47
Nata.show()
       

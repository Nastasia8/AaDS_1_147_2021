class Animal:
    def __init__(self,name):
        self.__name = name

    def speak(self, voice):
        raise NotImplementedError("Класс наследник должен реализовать данный метод")

    @property
    def name(self):
        return self.__name

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.__age = 1
    def speak(self, voice):
        print(self.name, "is saying", voice)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            if age > 0 and age < 25:
                self.__age = age
            else:
                print("hhhh!")
        else:
            print("fjdadhfjkahdkfjh") 

    def show(self):
        print("name:", self.name , "age:", self.age)

class Cat(Animal):
    def __init__(self, name, color):
        self.__color = color

    def speak(self, voice):
        self.__voice = voice

    def show(self):
        print("name:", self.name , "color:", self.__color)

cat =  Cat("lilya", "grey")
cat.speak("meow")
cat.show()
dog = Dog("Jerry")
dog.speak("gav")
dog.show()

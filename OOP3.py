class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what to say because I do not know what I am")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

######################################################################################

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 31)
c.speak()
d = Dog("Jill", 55)
d.speak()
f = Fish("Bubbles", 10)
f.speak()

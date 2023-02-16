
# Youtube Link: https://www.youtube.com/watch?v=JeznW_7DlB0
# Timestamp left off last: 13:09

# To clear the terminal everytime
import os
os.system('cls')


##################################
class Dog: # We name the class over here
    
    def __init__(self, name, age):    # This is run whenever an instance such as "d" is called. This basically runs everytime
        self.name = name         # This stores the name of the dog so that we can access it later
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
    
    def add_one(self, x):
        return x + 1

    def bark(self):        # All methods(actions) start with a parameter called self
        print("bark")
##################################################################


# This is where the actual code rlly starts
d = Dog("Tim", 43) # This defines the variable "d" as a dog. Now this "d" can do methods such as "bark"
d.set_age(5)
print(d.get_name())
print(d.get_age())
d2 = Dog("Bill", 54) # "Bill" defines the name of the dog as it is called upon instantly when the class is called
print(d2.get_name())
print(d2.get_age())

# d.bark()  # This is where the instance "d" is called and then the fuction is given for "d" to bark which prints out "bark"
# print(type(d))
# print(d.add_one(3))



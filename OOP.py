
# To clear the terminal everytime
import os
os.system('cls')


##################################
class Dog: # We name the class over here
    
    def __init__(self, name):    # This is run whenever an instance such as "d" is called. This basically runs everytime
        self.name = name         # This stores the name of the dog so that we can access it later
        print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):        # All methods(actions) start with a parameter called self
        print("bark")
##################################################################


# This is where the actual code rlly starts
d = Dog("Tim") # This defines the variable "d" as a dog. Now this "d" can do methods such as "bark"
d2 = Dog("Bill") # "Bill" defines the name of the dog as it is called upon instantly when the class is called

d.bark()  # This is where the instance "d" is called and then the fuction is given for "d" to bark which prints out "bark"
print(type(d))
print(d.add_one(3))
print(d.name)
print(d2.name)
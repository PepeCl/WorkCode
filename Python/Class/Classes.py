class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello my name is " + self.name)

person1=Person("Giuseppe",32)

person1.myFunc()
print(person1.age)
class Person:
    def __init__(self):
        self.name=input("Enter the name \n")


    def display_information_fn(self):
        print(f"Name is {self.name}")


person1=Person()
person1.display_information_fn()

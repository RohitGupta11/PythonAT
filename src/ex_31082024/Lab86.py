class dog:
    name=None
    breed=None
    Color=None

    def sleep(self):
        print("sleeping")

    def bark(self):
        print("bark")

    def eat(self):
        print("i am eating")

dog1=dog()
print(dog1.name)
dog1.name="chow"
print(dog1.name)
dog1.sleep()

print("------")

dog2=dog()
print(dog2.name)
dog2.name="maltas"
print(dog2.name)
dog1.sleep()

dog3=dog2
dog3.bark()
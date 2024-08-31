#constructor
#special function in class, __init()__()
#it will be automaticallu calld when object created

class Dog:
    name=None
    age=None

    def __init__(self,name,age):
        print("DC| I will called autmatically when object are created")
        self.name=name
        self.age=age


    def sleep(self):
       print ("i m sleeping")
       print("who is sleeping->",self.name,self.age)

dog1=Dog("chow",20)
print(dog1.name)
dog1.sleep()

dog2=Dog("maow",15)
dog2.sleep()
print(dog2.name)

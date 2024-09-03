#encapsulation
class car:
    name=None
    password=123

    def __init__(self):
        print("dc")

    def changepassword(self):
        self.password="parmod"

    def changepassowrd2(self):
        print(self.password)
objref=car()
print(objref.password)
objref.changepassword()
objref.changepassword2()


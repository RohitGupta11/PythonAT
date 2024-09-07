class Father:
    a=10
    def home(self):
        print("1bhk")

class son(Father):
    def home(self):
        super().home()
        print(super().a)
        print("no house")

pramod=son()
pramod.home()
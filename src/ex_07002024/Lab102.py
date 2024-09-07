#method overloading
class Shape:
    def area(self):
        print("area of rectangle:")


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

shap1=Rectangle(3,4)

print(shap1.area())
shap2=circle(3)
print(shap2.area())



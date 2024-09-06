class Parent:
    gold="gold"
    def bhk2(self):
        print("2BHK")

class child(Parent):
    diamond="diamond"
    def BHK3(self):
        print("3bhk")

child_obj=child()
child_obj.bhk2()
child_obj.BHK3()
print(child_obj.gold)
parent_ob=Parent()
parent_ob.bhk2()
#parent_ob.BHK3()
#print(parent_ob.diamond)
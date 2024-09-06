class Father:
    key = "2BHK"


    def car(self):
        print("father car!!", "alto")
        print("father car1!!", "alto", self.key)


class Son(Father):
    pass



obj = Father()
obj.car()
print(obj.key)

objs = Son()
objs.car()

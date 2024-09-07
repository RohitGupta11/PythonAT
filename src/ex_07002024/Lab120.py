#static method

class Mathoperations:
    def div(selfa,a,b):
        return a/b

    @staticmethod
    def sum(a,b):
        return a+b


obj=Mathoperations()
print(obj.div(10,5))
print(Mathoperations.sum(10,5))
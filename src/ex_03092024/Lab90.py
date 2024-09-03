class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = calculator(30,2)
ouputsum = cal1.sum()
ouputsub = cal1.sub()
ouputmul = cal1.mul()
ouputdiv = cal1.div()

print(ouputsum, ouputsub, ouputmul, ouputdiv)

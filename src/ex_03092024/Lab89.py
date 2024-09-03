class calculator:
    def __init__(self):
        print("dc")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


cal1 = calculator()
a = int(input("Enter the numer1:\n"))
b = int(input("Enter the numer2:\n"))
ouputsum = cal1.sum(a, b)
ouputsub = cal1.sub(a, b)
ouputmul = cal1.mul(a, b)
ouputdiv = cal1.div(a, b)

print(ouputsum, ouputsub, ouputmul, ouputdiv)

#multilevl inheritance
class Grandfather:
    gold="2kg"


    def bhk1(self):
        print("1BHK")

class Father(Grandfather):
    diamond="22 karat"

    def bhk2(self):
        print("2BHK")

class son(Father):
    btc="1BTC"

    def bhk3(self):
        print("3BHK")

s=son()
s.bhk1()
print(s.gold)
print(s.diamond)
print(s.btc)
s.bhk3()

s.bhk2()
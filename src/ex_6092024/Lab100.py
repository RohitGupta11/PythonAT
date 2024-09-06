#Multiple inheritance

class Father:

    def father_money(self):
        return 10

    def home(self):
        return  "this is from father"

class Mother:

    def mother_money(self):
        return 2

    def home(self):
        return  "this is from mother"


class son(Mother,Father):
    pass

s=son()
print(s.father_money())
print(s.mother_money())
print(s.home())

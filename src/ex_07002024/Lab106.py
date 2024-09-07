from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def loan(self):
        pass

class Pramod(Father):
    def loan(self):
        print("paid the loan")


objofpramod=Pramod("pp")
objofpramod.loan()
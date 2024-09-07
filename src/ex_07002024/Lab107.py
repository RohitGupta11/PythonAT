from abc import ABC, abstractmethod

class PyATB(ABC):
    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Amit(PyATB):
    def payFee(self):
        print("paid")

amitobj=Amit()
amitobj.payFee()
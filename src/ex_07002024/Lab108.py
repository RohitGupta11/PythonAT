from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(Engine):

    def start(self):
        print("starting")

    def stop(self):
        print("stoping")

    def drive(self):
        self.start()
        self.stop()

carobj=car()
carobj.drive()

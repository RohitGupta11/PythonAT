from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readFromexcel(self):
        pass

class browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(browser):
    def startBrowser(self):
        print("starting browser")

    def stopBrowser(self):
        print("stoping browser")

    def readFromexcel(self):
        print("reading from excel ")

    def runtestcase(self):
        self.startBrowser()
        self.readFromexcel()
        self.stopBrowser()
tc1ob=TC1()
tc1ob.runtestcase()




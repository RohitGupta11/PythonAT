class person:
    #attribute
    id=None
    name=None
    age=None
    email=None
    height=None
    gender=None
    phone_no=None
    address=None


    #behaviours
    def talk(self):  #self-this,self will be first argument in every behaviour
        print("I talk")

    def sleep(self, name):  #arg with return
       print("I am method")
       return None

    def walk(self):
        print("I am walking")

    def walk_return(self): #No-arg with return
        return "I am walking"

#create objcet of the class
#objectRef=classNmae()->object

tushar=person()
tushar.name="tushar"
print(tushar.name)
tushar.talk()

Rajyalaxmi=person()
Rajyalaxmi.name="Rajyalxmi"
Rajyalaxmi.talk()
print(Rajyalaxmi.name)


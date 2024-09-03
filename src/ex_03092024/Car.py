class car:
    def __init__(self,o_name,o_make,o_model):
        self.o_name=o_name
        self.o_make=o_make
        self.o_model=o_model

    def startengine(self):
        print("starting carwith name:"+self.o_name)
        print("starting carwith name:"+self.o_make)
        print("starting carwith name:"+self.o_model)

lambo=car("lambo","v2","2024")
lambo.startengine()


suv=car("suv","lv2","2026")
suv.startengine()



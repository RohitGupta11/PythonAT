class MathUtils(object):

    def add(self,a,b):
        return  a+b

    def add(self,a,b,c=0):
        return  a+b+c

math=MathUtils()
op1=MathUtils.add(1,3,4)
print(op1)
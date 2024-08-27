#fiunction scope
global_b=12   #gloabal variable
def my_function():
    a=10   #local variable within the fn
    print(a)

def f1():
    print(global_b)

my_function()
print(global_b)
f1()


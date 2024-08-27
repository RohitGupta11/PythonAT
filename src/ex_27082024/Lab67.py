# decorators in python
def my_decorators(func):
    # two parts
    # 1. wrap 2. call
    def wrapper():
        print("something is happening before the function is called:")
        print("add helmet,gloves,knee guards")
        func()  #drive_bike()
        print("something is happening after the function is called:")
        print("secure driving")

    return wrapper()

@my_decorators
def drive_bike():
    print("i m driving")


#drive_bike()

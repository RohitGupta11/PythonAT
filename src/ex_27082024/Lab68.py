# @staticmethod
# @classmethod
# @propertymethod
# @functoolsmethod
# we will understand in oops

# chaining decoratoors
def decorators(func):
    def wrapper():
        print("decorato1")
        func()

    return wrapper()


def decorators2(func):
    def wrapper():
        print("decorator2")
        func()

    return wrapper()


@decorators
@decorators2
def say():
    print("hello")


say()
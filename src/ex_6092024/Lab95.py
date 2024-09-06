class Myclass:
    public_var="I am public"

    __private_var="I am private"
    _protected_var="i am protected"


object=Myclass()
print(object.public_var)
print(object._protected_var)
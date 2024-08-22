usertype=input("Enter the usertype,admin,manager,guest: ")
usertype=usertype.lower()
match usertype:
    case "admin"|"manager":
        print("Hello sir")
    case "guest":
        print("Hello guest")
    case _:
        print("Hello there")


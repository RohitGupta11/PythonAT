# Match statment
# switch in java
# match the and execute
#python>3.10


#wap to ask the user which browser he want to run automation

browser_name=input("enter the name of browser:\n")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the Chrome code")
    case "edge":
        print("Execute the Edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found")


def print_arguments(*args):
    print(args[0])
    for i in args:
        print(i)

print_arguments("parmod","rohit","lucky")

print_arguments("parmod","rohit",10,32.1,True)

#print_arguments("parmod")
#print_arguments()//error
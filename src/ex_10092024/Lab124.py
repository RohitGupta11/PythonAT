#try except finally
try:

   a=int(input("enter the num1:"))
   b=int(input("enter the num2:"))
   c=a/b

except  ValueError as ve:
    print(" ValueError, you enter the string instead of number")

except  ZeroDivisionError as ze:
    print("ZeroDivisonError,you are dividing with zero")
else:
    print("result of  div:", c)


finally:
    print("this will awlys executable")

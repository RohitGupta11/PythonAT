print("start  of the program")
try:

   a=int(input("enter the num1:"))
   b=int(input("enter the num2:"))
   c=a/b
   print("result of  div:", c)

except  Exception as e:
    print(e)
    print("please check your input , it shpuld not be zero or string")

print("end  of the program")

#try
    #try this code if error
#except
    #execute me if try have some error
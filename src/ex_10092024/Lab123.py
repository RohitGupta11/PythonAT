#try
    #try this code if error
#except
    #execute me if try have some error
import  math
try:
   math.exp(1000)
except Exception as e:
    print(e)
    print("pls try to use lower exponential value")
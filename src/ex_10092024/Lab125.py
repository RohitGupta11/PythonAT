#try except finally
#file

import os
try:
   file=open('example.txt', 'r')
   print(file.read())
except FileNotFoundError as fnfe:
    print("file no found,fix the file or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

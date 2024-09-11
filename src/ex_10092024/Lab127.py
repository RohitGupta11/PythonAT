
try:
   file=open('example.txt','r')
   content=file.read()
   print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

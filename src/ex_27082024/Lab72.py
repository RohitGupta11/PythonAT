# def sumofthree(a,b,c):
#     return a+b+c

sum=lambda a,b,c:a+b+c
print(sum(1,2,3))
#
# def find_even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")

check_even_odd=lambda num: "even" if num%2==0 else "odd"
print(check_even_odd(30))
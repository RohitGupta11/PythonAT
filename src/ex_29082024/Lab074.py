#List
#list is collectionof items(duplicates)
my_list=[1,2,3]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[2])
#print(my_list[10]) #IndexError: list index out of range-execeptions
my_list[0]="prmod"
my_list[1]="rohit"
my_list[2]="parmod"

print("element at the index 0 -", my_list[0])
print("element at the index 0 -", my_list[1])
print("element at the index 0 -", my_list[2])

print(my_list)

for element in my_list:
    print(element)

print("____________________")

#append()
my_list.append(4)
my_list.append(12.6)
print(my_list)

#extend()
my_list.extend(["naina",4,5,6,7,8])
print(my_list)


#insert() ->in between add
my_list.insert(1,"dutta")
print(my_list)
print(len(my_list))

my_list[1]="43"
print(my_list)

#remove()
my_list.remove("naina")
print(my_list)

#copylist
my_cpiedlist=my_list.copy()
my_list.clear()
print(my_list)
print(my_cpiedlist)

#my_cpiedlist.sort()
#print(my_cpiedlist)

my_cpiedlist.reverse()
print(my_cpiedlist)

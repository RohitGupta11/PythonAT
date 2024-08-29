t1=("TheTestingAcademy","for","TheTestingAcademy")
print(set(t1))


#union
set1={1,2,3}
set2={4,5,6}
set3=set1.union(set2)
print(set3)

#intersection
set1={1,2,3}
set2={2,3,6}
set3=set1.intersection(set2)
print(set3)


#differnce
set1={1,2,3}
set2={2,3,6}
#set3=set1.difference(set2)
set3=set2.difference(set1)
print(set3)

#subset
set1={1,2,3,4,5,6}
set2={2,3,8}
set3=set1.issubset(set2)
print(set3)




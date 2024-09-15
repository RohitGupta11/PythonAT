#ordered dictionary

from collections import OrderedDict, defaultdict

d={"id":123, "name":"rpohit", "age":89, "state":"Delhi"}
print(d)

d2=dict()
d2["age"]=45
d2["name"]="rohit"
d2["salary"]=1000
print(d2)

od=OrderedDict()
od['banana']=2
od['apple']=1
od['pear']=3
print(od)

dd=defaultdict(int)
print(dd)
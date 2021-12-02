from django.test import TestCase

# Create your tests here.

list2 = [{"0":{"A1":"a1","B1":"b1"}},{"1":{"A2":"a2","B2":"b2"}},{"2":{"A3":"a3","B3":"b3"}}]   
list_v=[x for x in list2 ]
print(list_v)

l=[x.get(str(i)) for i,x in enumerate(list2)]
print("lit=",l)

mlist=[list2[x].get(str(x)) for x in range(0,len(list2))]
print(mlist)

# data={}
# for dic in list2:
#     data.update(dict(dic))
   
# m={}
# for k,v in data.items():
#     m.update(v)
# jj={}
# jj.update([x for x in list2 for k,v in (dict(x)).items()])
# print(res)

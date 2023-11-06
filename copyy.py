what is the difference between shallow copy and deep copy?
if we want to perform shallow copy and deep copy then we have to import copy module. copy module contains copy() method and deepcopy() method.
by using that we can perfrom shallow copy and deepcopy.
shallow copy: shallow copy does not creagte new object and in the original list if we modify(means insert,update,remove) any immutable elements (like numbers,strings)
then those changes will not be affected in the shallow copy. however, if we modify(means insert,update,remove) any mutable elements
(like lists, dictionaries) in the original list then those changes will be affected in the both shallow
copy and original list because they both reference the same inner mutable objects.

deepcopy:
deep copy creates a new object and in original list if we modify (means insert,update,remove) any mutable and immutable elements then those changes will not be affected in the deep copy.
because deep copy creates an independent set of objects.

example1:
import copy
original_list=[1,2,[3,4]]
shallow_copy=copy.copy(original_list)
deep_copy=copy.deepcopy(original_list)
original_list[2][0]=999
print("original list is=",original_list,id(original_list),id(original_list[2][0]))
print("shallow copy is=",shallow_copy,id(shallow_copy),id(shallow_copy[2][0]))
print("deep copy is=",deep_copy,id(deep_copy),id(deep_copy[2][0]))
output:
original list is= [1, 2, [999, 4]] 2618434720448 2618465149680
shallow copy is= [1, 2, [999, 4]] 2618434720768 2618465149680
deep copy is= [1, 2, [3, 4]] 2618434721728 2618428490032

example2:
import copy
original_list=[1,2,[3,4]]
shallow_copy=copy.copy(original_list)
deep_copy=copy.deepcopy(original_list)
original_list[0]=999
print("original list is=",original_list,id(original_list),id(original_list[2][0]))
print("shallow copy is=",shallow_copy,id(shallow_copy),id(shallow_copy[2][0]))
print("deep copy is=",deep_copy,id(deep_copy),id(deep_copy[2][0]))
output:
original list is= [999, 2, [3, 4]] 1983409623744 1983403393328
shallow copy is= [1, 2, [3, 4]] 1983409624064 1983403393328
deep copy is= [1, 2, [3, 4]] 1983409625024 1983403393328


another example:
from copy import copy,deepcopy
x=1000
y=[1000,2000,3000]
z="hyd"
a=[x,y,1000,2000,3000,z]
k=a
l=[1000,2000,3000]
m=a[:]
n=deepcopy(a)
o=copy(a)
a.remove(3000)
print(m)
print(n)
print(k)
print(a)
output:
[1000, [1000, 2000, 3000], 1000, 2000, 3000, 'hyd']
[1000, [1000, 2000, 3000], 1000, 2000, 3000, 'hyd']
[1000, [1000, 2000, 3000], 1000, 2000, 'hyd']
[1000, [1000, 2000, 3000], 1000, 2000, 'hyd']

another example:
from copy import copy,deepcopy
a=[[3000,4000],1000,2000]
b=a[:]
d=copy(a)
e=a
c=deepcopy(a)
a[1]=6000
print(a[1])
print(b[1])
print(c[1])
print(d[1])
print(e[1])
output:
6000
1000
1000
1000
6000




























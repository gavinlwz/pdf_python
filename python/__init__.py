a={1,2,3}
b=a
c=a.copy()
import copy
d=copy.copy(a)



print(id(a),id(b),id(c),id(d))
a.union({'a'})
print()
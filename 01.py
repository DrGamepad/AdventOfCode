import res
from functools import reduce
from itertools import combinations

a =[int (x) for x in res.read_File ()]
a.sort ()
b = a.copy ()

a = reduce (lambda x,y: x*y, [x for x in a if (2020-x) in a])
b = [ ( y[0]* y[1] * y[2]) for y in list (combinations ([x for x in b if x < (2020 - sum (b [:2]))],3)) if sum (y) == 2020].pop ()

print (a,b)

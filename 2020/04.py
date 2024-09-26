import sys
sys.path.append('..')

import res
import itertools
a =[x for x in res.read_File ("input04.txt")]
b = a.copy ()

a = [list(y) for x, y in itertools.groupby(a, lambda z: z == '') if not x]

for i in a:
	print (i)

#a = []
#b = []

#print ("1.) " + str(a) + "\n2.) " + str(b))
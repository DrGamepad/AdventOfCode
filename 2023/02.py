import sys
sys.path.append('..')
import res
import re

a =[re.sub('Game \b([0-9]|[1-9][0-9]|100)\b: ', '', x) for x in res.read_File ("input02.txt")]
b = a.copy ()

for i in a: print (i)

#print ("1.) " + str(a) + "\n2.) " + str(b))
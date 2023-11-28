import sys
sys.path.append('..')
import res

a =[int (x) for x in res.read_File ("input01.txt")]
a.sort ()
b = a.copy ()

a = []
b = []

print ("1.) " + str(a) + "\n2.) " + str(b))
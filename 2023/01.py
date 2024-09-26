import sys
sys.path.append('..')
import res
import re

txt = [x for x in res.read_File ("input01.txt")]

num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

a =[int(''.join([re.sub("[^0-9]","",x)[i] for i in (0, -1)])) for x in txt]
#a.sort ()

#b = [[i] for elem in txt for i in range(len(elem)) if elem.startswith('one', i)]

b = map()

#[i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]

#for x in a: print([x[i] for i in (0, -1)])

print (b)

print ("1.) " + str(sum(a)) + "\n2.) " + str(0))
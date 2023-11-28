import sys
sys.path.append('..')
import res
import pandas as pd

a =[x for x in res.read_File ("input03.txt")]
a = [list(x*32) for x in a]

df = pd.DataFrame(a)

j = 3
t = 0
"""
for i in range(len(a)):
	#print (str(j) + "/" + str(i))
	df.at[i,j] = 'X'
	j += 3
"""


for i in range(1,len(a)):
	if df.iat[i,j] == '#':
		df.at[i,j] = 'X'
	else:
		df.at[i,j] = '0'
	j += 3
	#j += 3
	#print(str(j//3) + "/" + str(len(a)) + ":" + i[j])
	#print (str(j) + "/" + str(len(a[0])) + ": " + i[j])
print (df)
print((df == 'X').sum().sum())
print((df == '0').sum().sum())

#for i in a:
# print (i)
#print ("1.) " + str(a) + "\n2.) " + str(b))

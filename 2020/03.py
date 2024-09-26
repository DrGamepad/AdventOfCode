import sys
sys.path.append('..')
import res
import pandas as pd

a =[x for x in res.read_File ("input03.txt")]
a = [list(x*32) for x in a]

df = pd.DataFrame(a)

j = 3
t = 0
for i in range(1,len(a)):
	if df.iat[i,j] == '#':
		df.at[i,j] = 'X'
	else:
		df.at[i,j] = '0'
	j += 3
print(df)
print((df == 'X').sum().sum())
print((df == '0').sum().sum())

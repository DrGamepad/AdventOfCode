import res

i = 0
a = [int (x) for x in res.read_File ("input01.txt")]
for x in range(len(a)-1):
    if a[x] < a[x+1]:
        i = i+1
print (i)

import res

i = 0
a = [int (x) for x in res.read_File ("input01.txt")]
b= [a[x] + a[x+1] + a[x+2] for x in range(len(a)-2)]
for x in range(len(b)-1):
    if b[x] < b[x+1]:
        i = i+1
print (i)

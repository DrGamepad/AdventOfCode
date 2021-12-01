import res

a = [ int (x) for x in res.read_File("input01.txt")]
print( len( [ x for x in range( len(a) - 1) if a[x] < a[x + 1]]))

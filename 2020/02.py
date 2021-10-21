import res

def truePass (x):
    return x [2].count (x [1] [:1]) >= int (x [0].split ('-') [0]) and x [2].count (x [1] [:1]) <= int (x [0].split ('-') [1])

print ([truePass (y) for y in [x.split () for x in res.read_File ("input02.txt")]].count (True))

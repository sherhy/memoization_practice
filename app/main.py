memo = {}

def main(argv):    
    fileName = argv[3]
    x = int(argv[0])
    y = int(argv[1])
    z = int(argv[2])

    with open(fileName, 'a+') as f:
        text = f.read()
        f.write(text)
        f.write(str(x)+','+str(y)+','+str(z)+'\n')    
    return newRec(x,y,z,fileName)        

def newRec(x,y,z,fileName):
    if x<= y:
        return y
    else:
        var1 = 0
        var2 = 0
        var3 = 0    
        if ((x-1, y, z) in memo):
            var1 = memo[(x-1, y, z)]
        else:
            res1 = newRec(x - 1, y, z, fileName)
            memo[(x-1, y, z)] = res1
            var1 = res1
        if ((y-1, z, x) in memo):
            var2 = memo[(y-1, z, x)]
        else:
            res2 = newRec(y-1, z, x, fileName)
            memo[(y-1, z, x)] = res2
            var2 = res2
        if ((z - 1, x, y) in memo):
            var3 = memo[(z - 1, x, y)]
        else:
            res3 = newRec(z - 1, x, y, fileName)
            memo[(z - 1, x, y)] = res3
            var3 = res3
        return main([var1, var2, var3, fileName])
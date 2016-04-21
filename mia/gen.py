#do not give to competitors
hexflag = "66 6c 61 67 7b 6d 31 53 73 31 6e 67 5f 31 4e 5f 34 63 54 31 30 6e 7d".replace(" ", "")
c = 0
encrypt = [['0','1','2','3'],['4','5','6','7'],['8','9','a','b'],['c','d','e','f']]
while c < len(hexflag):
    encrypt = [['0','1','2','3'],['4','5','6','7'],['8','9','a','b'],['c','d','e','f']]
    fs = open('file'+str(c)+".txt", 'w')
    if hexflag[c] in encrypt[0]:
        encrypt[0][encrypt[0].index(hexflag[c])] = "*"
    if hexflag[c] in encrypt[1]:
        encrypt[1][encrypt[1].index(hexflag[c])] = "*"
    if hexflag[c] in encrypt[2]:
        encrypt[2][encrypt[2].index(hexflag[c])] = "*"
    if hexflag[c] in encrypt[3]:
        encrypt[3][encrypt[3].index(hexflag[c])] = "*"
    encrypt[0] = " ".join(encrypt[0])
    encrypt[1] = " ".join(encrypt[1])
    encrypt[2] = " ".join(encrypt[2])
    encrypt[3] = " ".join(encrypt[3])
    print "\n".join(encrypt)
    fs.write("\n".join(encrypt))
    c += 1
fs.close()

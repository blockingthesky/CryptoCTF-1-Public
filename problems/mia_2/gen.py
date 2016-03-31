#do not give to competitors
import md5
m = md5.new()
hexflag = ""
flag = "flag{m1ssing_y3t_4ga1n?}"
c = 0
while c < len(flag):
    m = md5.new(flag[c])
    hexflag = hexflag + m.hexdigest()
    c += 1
print hexflag
c = 0
while c < len(hexflag):
    encrypt = [['f','e','d','c'],['b','a','9','8'],['7','6','5','4'],['3','2','1','0']]
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
    #print "\n".join(encrypt)
    fs.write("\n".join(encrypt))
    c += 1
fs.close()

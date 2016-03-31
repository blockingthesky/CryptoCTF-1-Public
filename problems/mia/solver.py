#do not give to competitors
#throws an error at the end but it prints the hex encoded flag before that :P
c = 0
out = ""
while True:
    fs = open("file"+str(c)+".txt", 'r')
    inp = fs.read().split("\n")
    c1 = 0
    while c1 < 4:
        inp[c1] = inp[c1].split(" ")
        c1 += 1
    c1 = 0
    c2 = 0
    while c1 < 4:
        c2 = 0
        while c2 < 4:
            if inp[c1][c2] == "*":
                out = out + hex(4*c1 + c2)[2]
            c2 += 1
        c1 += 1
    print out
    c += 1
    fs.close()

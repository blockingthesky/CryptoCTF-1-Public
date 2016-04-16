import Image, random

def randcol():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

flag = Image.open('emptyflagged.png')
flag_pix = flag.load()
print flag.size
out1 = Image.new('RGB', flag.size, 'white')
out1_pix = out1.load()
out2 = Image.new('RGB', flag.size, 'white')
out2_pix = out2.load()
wid = flag.size[0]
hei = flag.size[1]
for c in range(wid):
    for r in range(hei):
        toc = randcol()
        out1_pix[c,r] = toc
        if flag_pix[c,r] == (0, 0, 0):
            out2_pix[c,r] = toc
        else:
            out2_pix[c,r] = randcol()

out1.save('firstout.png')
out2.save('secondout.png')

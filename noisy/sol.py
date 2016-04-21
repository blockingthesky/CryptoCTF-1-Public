import Image
inp1 = Image.open('firstout.png')
pix1 = inp1.load()
inp2 = Image.open('secondout.png')
pix2 = inp2.load()

out = Image.new('RGB', inp1.size, 'white')
pix = out.load()

wid = inp1.size[0]
hei = inp2.size[1]

for c in range(wid):
    for r in range(hei):
        if pix1[c,r] == pix2[c,r]:
            pix[c,r] = (0, 0, 0)

out.save('flagout.png')

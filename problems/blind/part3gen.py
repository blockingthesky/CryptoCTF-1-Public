import Image, random
img = Image.open('part3.png')
pix = img.load()
for i in range(1200):
    for j in range(626):
        f = pix[i,j][:3]
        if f == (1, 1, 1):
            pix[i,j] = random.choice([(1, 1, 0), (0, 1, 1)])

img.save('part3comp.png')

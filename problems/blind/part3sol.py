import Image, random
img = Image.open('part3comp.png')
pix = img.load()
for i in range(1200):
    for j in range(626):
        f = pix[i,j][:3]
        if f == (0,1,0) or f == (1,0,0):
            pix[i,j] = (255, 255, 255)

img.save('part3sol.png')

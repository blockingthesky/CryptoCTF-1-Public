import Image

img = Image.open('useless.png')
w,l = img.size
pix = img.load()

for i in range(w):
    for j in range(l):
        if sum(pix[i,j]) % 2 == 0:
            pix[i,j] = (255,255,255)
        else:
            pix[i,j] = (0,0,0)

img.show()

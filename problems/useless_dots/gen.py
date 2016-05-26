import Image, random

img = Image.open('flag.png')
pix = img.load()
w,l = img.size

def rcol(odd):
    ret = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    if odd == sum(ret) % 2:
        return ret
    else:
        return rcol(odd)

for i in range(w):
    for j in range(l):
        pix[i,j] = rcol(pix[i,j][:3] == (255, 255, 255))

img.save('useless.png')
            

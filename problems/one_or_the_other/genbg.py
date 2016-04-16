import Image, random

def randcol():
    return tuple([random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)])


img = Image.new('RGB', (1200, 300), 'white')
pix = img.load()

for i in range(1200):
    for j in range(300):
        pix[i, j] = randcol()
        
img.save('crypto_rox.png')
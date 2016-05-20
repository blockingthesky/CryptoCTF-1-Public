import Image
img = Image.new('RGB', (1200, 626), 'white')
pix = img.load()
for i in range(1200):
    for j in range(626):
        if (i + j) % 2 == 0:
            pix[i,j] = (0, 1, 0)
        else:
            pix[i,j] = (1, 0, 0)

img.save('part3.png')

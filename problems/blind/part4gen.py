import Image, random
pos = [(1, 0, 0),(0, 1, 0),(0, 0, 1),(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 0)]
img = Image.new('RGB', (1200, 626), 'white')
pix = img.load()
for i in range(1200):
    for j in range(626):
        pix[i,j] = random.choice(pos)

img.save('part4.png')

import Image, sys

img1 = Image.open(sys.argv[1])
pix1 = img1.load()
img2 = Image.open(sys.argv[2])
#img2 = Image.new('RGB', img1.size, 'white')
pix2 = img2.load()

W, H = min(img1.size, img2.size)
for w in range(W):
    for h in range(H):
        pix1[w,h] = tuple(k[0] ^ k[1] for k in zip(pix1[w,h], pix2[w,h]))
        
if sys.argv[3] == 'show':
    img1.show()
else:
    img1.save(sys.argv[3])
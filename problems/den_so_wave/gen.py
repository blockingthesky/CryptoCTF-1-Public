import Image

img = Image.open('qrcode.png')
pix = img.load()
ret = ''
for i in range(img.size[0]):
    for j in range(img.size[1]):
        ret += str(pix[i,j])

open('den_so_wave.txt', 'w').write(ret)

import Image
inp = open('message.txt', 'r')
img = Image.new('RGB', (200, 50), 'white')
pix = img.load()
for m in inp.readlines():
    m = [int(n) for n in m.strip().split(",")]
    pix[m[0],50-m[1]] = (0, 0, 0, 0)

img.show()
    

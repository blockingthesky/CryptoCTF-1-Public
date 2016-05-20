from PIL import Image
import random
img = Image.new('RGB', (128, 128), 'white')
pix = img.load()

msg = open('message', 'r').readline().strip()
col = [0, 0, 0]
def ncol(p):
    dist = ord(p)
    a = random.randint(0, dist)
    dist -= a
    b = random.randint(0, dist)
    dist -= b
    c = dist
    global col
    col[0] += a
    col[1] += b
    col[2] += c
    col[0] %= 256
    col[1] %= 256
    col[2] %= 256
    
for i in range(128):
    for j in range(128):
        if i == 0 and j == 0:
            pix[i,j] = (0, 0, 0)
        else:
            ncol(msg[(128*i)+j])            
        if i % 2 == 0:
            pix[j,i] = tuple(col)
        else:
            pix[127-j,i] = tuple(col)

img.save('pixels.png')

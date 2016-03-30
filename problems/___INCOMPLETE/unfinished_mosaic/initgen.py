import Image, random

def colorgen():
    return tuple([random.randint(1, 254),random.randint(1, 254),random.randint(1, 254)])

img = Image.new( 'RGB', (256*3,75), "white") # create a new black image
pixels = img.load() # create the pixel map

used = set()

while len(used) < 255:
    used.add(colorgen())

for m in range(75):
    pixels[0, m] = (0, 0, 0)
    pixels[256*3-1, m] = (0, 0, 0)    

for k in range(1, 255):
    st = used.pop()
    beg = random.randint(45, 70)
    for m in range(beg, beg + 5):
        pixels[3*k, m] = st
        pixels[3*k - 1, m] = st

for j in range(1, 256*3):
    for h in range(random.randint(0, 50)):
         y = random.randint(0, 74)
         if pixels[j, y] == (255, 255, 255): 
             pixels[j, y] = colorgen()
    

'''
for i in range(img.size[0]/2):    # for every pixel:
    for j in range(img.size[1]/2):
        pixels[i,j] = (i, j, 0) # set the colour accordingly
        pixels[i+255,j] = (i, j, 75) # set the colour accordingly
        pixels[i,j+255] = (i, j, 150) # set the colour accordingly
        pixels[i+255,j+255] = (i, j, 225) # set the colour accordingly
'''

img.show()

img.save('shufflegen.png')

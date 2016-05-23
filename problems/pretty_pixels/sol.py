from PIL import Image

# Open the picture
pix = Image.open('pixels.png').load()

# Hold all the pixels from our traversal
pixels = []
'''
Traverse from top to bottom in a zig-zag pattern, like so:

---->---->---->---->----+
                        |
+---<----<----<----<----+
|
---->---->---->---->----+
                        |
+---<----<----<----<----+
|
+--->-- etc.
'''
for i in range(128):
    for j in range(128):
        if i % 2 == 0:
            pixels.append(pix[j, i])
        else:
            pixels.append(pix[127 - j, i])

# Compute the sum of the differences of each R, G, and B value.
# A step from 255 to 0 is 1, 254 to 3 would be 5, etc.
def dif(pixel_a, pixel_b):
    return sum(i % 256 for i in [pixel_b[0] - pixel_a[0], pixel_b[1] - pixel_a[1], pixel_b[2] - pixel_a[2]])
    
# Find the difference between each pixel.
chars = [dif(pixels[t], pixels[t+1]) for t in range(len(pixels)-1)]
# Print message
print ''.join(chr(o) for o in chars)

# Create flag from chars
fleg = ''.join(chr(o) for o in chars)
# Print that shit
print fleg[fleg.index('flag{'):fleg.index('}') + 1]
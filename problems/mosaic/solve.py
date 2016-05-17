import Image, random

def colorgen():
    return tuple([random.randint(1, 254),random.randint(1, 254),random.randint(1, 254)])

img = Image.open('transmission.png')
pixels = img.load() # create the pixel map

blocks = []
for c in range(256):
    curb = []
    for m in range(75):
        row = []
        for k in range(3):
            row.append(pixels[3*c + k, m])
        curb.append(row)
    left = (0, 0, 0)
    right = (0, 0, 0)
    for m in range(70):
        if curb[m][0] != (255, 255, 255, 255) and len(set([curb[j][0] for j in range(m, m + 5)])) == 1:
            left = curb[m][0]
            break
    for m in range(70):
        if curb[m][2] != (255, 255, 255, 255) and len(set([curb[j][2] for j in range(m, m + 5)])) == 1:
            right = curb[m][2]
            break
    curb.append(left)
    curb.append(right)
    print str(c) + "--> LEFT: " + str(left) + "  RIGHT: " + str(right)
    blocks.append(curb)

ordered = []
cright = (0, 0, 0, 255)
while len(blocks) != 0:
    print len(blocks)
    for m in range(len(blocks)):
        if blocks[m][-2] == cright:
            cright = blocks[m][-1]
            ordered.append(blocks.pop(m)[:-2])
            break
    else:
        print "NO " + str(cright) + "??"
        exit()
print len(ordered)



img.show()

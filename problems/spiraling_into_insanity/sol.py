import Image

def right(x, y): return x+1, y
def down(x, y): return x, y-1
def left(x, y): return x-1, y
def up(x, y): return x, y+1

trav = [right, down, left, up]

def spiral(N):
    global trav
    from itertools import cycle
    move = cycle(trav)
    n = 1
    pos = 0,0
    step = 2

    yield pos

    while True:
        for p in range(2):
            trav = next(move)
            for p in range(step):
                if n >= N:
                    return
                pos = trav(*pos)
                n += 1
                yield pos
        step += 2

img = Image.open('spiral.png')
pix = img.load()

ott = ''

# the picture is 401x401
center = 200,200

# make sure we go far enough to hit the whole spiral, and then some.
cap = 401**2

try:
    for m in spiral(cap):
        color = pix[center[0]-m[0],center[1]-m[1]][:3]
        ott += chr(sum(color)/3)
except: # will quit when out of range
    pass

ind = ott.find('flag{')
print ott[ind:ott.find('}') + 1]
    

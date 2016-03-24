import Image, random

'''
borrowed from http://goo.gl/ekUrez
'''

def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

moves = [move_right, move_down, move_left, move_up]

def gen_points(end):
    from itertools import cycle
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 2

    yield n,pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n+=1
                yield n,pos

        times_to_move+=2

def gencolor():
    return tuple([random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)])

def avg(k):
    retcol = gencolor()
    while sum(retcol)/3.0 != k:
        retcol = gencolor()
    return retcol


size = 401

flag = open('themessage.txt', 'r').readline()

grid = [[' '] * size for i in range(size)]

cent = size/2

img = Image.new('RGB', (401, 401), 'white')
pix = img.load()
#80801
cur = 0
for m in gen_points(80801):
    if cur % 1000 == 0:
        print cur
    pix[cent - m[1][0], cent - m[1][1]] = avg(ord(flag[cur]))
    cur += 1
	
pix[400, 400] = tuple([0, 0, 0])

img.save('spiral.png')

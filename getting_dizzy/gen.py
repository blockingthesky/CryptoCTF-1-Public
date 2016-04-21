import math
text = "Why couldn't we just spiral from the top left like normal people? Always so gosh darn difficult. At least the number of characters was a perfect square, can you imagine if the center had been empty? You wouldn't have ever found this: flag{73706972616c735f6172655f66756e}. But, you did, so."
text = text[::-1]
print text

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
    times_to_move = 1

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

        times_to_move+=1

size = int(math.ceil(math.sqrt(len(text))))
gd = [[' '] * size for s in range(size)]
cent = [size/2, size/2]
for m in gen_points(len(text)):
    gd[cent[0] + m[1][0]][cent[1] + m[1][1]] = text[m[0] - 1]

open('message.txt', 'w').write(''.join([''.join(k) for k in gd]))

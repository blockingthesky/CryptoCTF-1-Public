import random

def decompose(num):
    ret = []
    while num > 4:
        k = random.choice([1, 2, 3, 4])
        num -= k
        ret.append(k)
    ret.append(num)
    return ''.join(str(u) for u in ret)

def lrzfill(word, width):
    togo = width - len(word)
    a = random.randint(0, togo)
    return (word.zfill(width - a)[::-1]).zfill(width)[::-1]

message = ("now i'm too lazy to even come up with "
           "a message to keep the flag in whoops it's"
           " 12:18 AM flag{never_make_problems_after_midnight}")
combs = [decompose(ord(p)) for p in message]
k = max(len(t) for t in combs)
combs = [lrzfill(y, k) for y in combs]
combs2 = [''.join(combs[p][i] for p in range(len(combs))) for i in range(k)]

for i in range(len(combs2)):
    with open('psychic3/psychic3_' + str(i) + '.lol', 'w') as rip:
        rip.write(combs2[i])

print 'donezo'

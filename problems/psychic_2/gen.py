import random

def xor_pair(num):
    k = random.randint(0, 255)
    return k, num ^ k

def gen_reduceable_string(final):
    ret = [final]
    size = random.randint(10000, 20000)
    for i in xrange(size):
        a, b = xor_pair(ret[-1])
        ret = ret[:-1] + [a, b]
    return ''.join(hex(u)[2:].zfill(2) for u in ret)

flag = "in the spirit of psychic problems, here's a Caesared flag: pvkq{e_bokn_wi_wsxn_agbslsfigso}"
for part in range(len(flag)):
    print part
    out = open('psychic_2_files/psychic2_' + str(part) + '.lol', 'w')
    out.write(gen_reduceable_string(ord(flag[part])))
    out.close()
print len(flag)
    

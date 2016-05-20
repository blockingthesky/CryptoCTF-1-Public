import random
primes = filter(lambda x: not any(x % i == 0 for i in range(2,128)), range(128, 1000))
flag = 'flag{digit_sum_problems_are_actually_my_favorite}'
nflag = [ord(u) * random.choice(primes) for u in flag]

def dig(num):
    ret = ''
    while num > 9:
        f = random.choice(range(10))
        ret += str(f)
        num -= f
    ret += str(num)
    return ret

out = open('maaaaaath.txt', 'w')
for n in range(len(flag)):    
    out.write(dig(nflag[n]) + ('\n' if flag[n] != '}' else ''))

out.close()

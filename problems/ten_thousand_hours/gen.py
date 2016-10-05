import random

flag = 'flag{r3ndomly_g3nerat3d_m3th0dS_FTW}'
k = len(flag)

tags = []
methods = []

def r(a, b):
    return random.randint(a, b)
    
def gentag():
    rettag = hex(r(0, 16**8 - 1)).replace('L', '')[2:].zfill(8)
    if rettag in tags:
        print "go buy a lottery ticket, shiet?"
        return gentag()
    else:
        tags.append(rettag)
        return rettag
        
def genarr(cap):
    return str([random.randint(1, cap) for i in range(k)])
    
def genkarr(cap):
    n = range(cap)
    random.shuffle(n)
    return str(n)
    
def gendsubarr():
    n = range(10)
    random.shuffle(n)
    return str([str(i) for i in n])
    
def gencarr():
    word = hex(r(0, 16**k - 1)).replace('L', '')[2:].zfill(k)
    return '[ord(p) for p in \'' + word + '\']'

# RANDOM PER INDEX
    
def genmul():
    mname = 'mul_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + genarr(r(3, 10)) + '\n    return [x[i] * y[i] for i in range(k)]'
    
def gensub():
    mname = 'sub_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + genarr(10**10) + '\n    return [x[i] - y[i] for i in range(k)]'
    
def genadd():
    mname = 'add_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + genarr(10**10) + '\n    return [x[i] + y[i] for i in range(k)]'
    
def genxor():
    mname = 'xor_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + genarr(10**10) + '\n    return [x[i] ^ y[i] for i in range(k)]'

# CONSTANT THROUGHOUT    

def gencmul():
    mname = 'cmul_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [x[i] * ' + str(r(3, 10)) + ' for i in range(k)]'
    
def gencsub():
    mname = 'csub_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [x[i] - ' + str(r(1, 10**10)) + ' for i in range(k)]'
    
def gencadd():
    mname = 'cadd_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [x[i] + ' + str(r(1, 10**10)) + ' for i in range(k)]'
    
def gencxor():
    mname = 'cxor_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [x[i] ^ ' + str(r(1, 10**10)) + ' for i in range(k)]'

# CHARACTER GENERATED

def genchmul():
    mname = 'chmul_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + gencarr() + '\n    return [x[i] * y[i] for i in range(k)]'
    
def genchsub():
    mname = 'chsub_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + gencarr() + '\n    return [x[i] - y[i] for i in range(k)]'
    
def genchadd():
    mname = 'chadd_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + gencarr() + '\n    return [x[i] + y[i] for i in range(k)]'
    
def genchxor():
    mname = 'chxor_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    y = ' + gencarr() + '\n    return [x[i] ^ y[i] for i in range(k)]'
    
# SHUFFLING METHODS

def genshuffle():
    mname = 'shuffle_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [x[p] for p in ' + genkarr(k) + ']'
    
def genchunk():
    mname = 'chunk_' + gentag()
    methods.append(mname)
    h = str(r(0, k))
    return 'def '  + mname + '(x):\n    return x[' + h + ':] + x[:' + h + ']'
    
def gendeck():
    mname = 'deck_' + gentag()
    a, b, c = (str(u) for u in sorted([r(0, k) for i in range(3)]))
    poss = ['x[:' + a + ']', 'x[' + a + ':' + b + ']', 'x[' + b + ':' + c + ']', 'x[' + c + ':]']
    random.shuffle(poss)
    return 'def ' + mname + '(x):\n    return ' + ' + '.join(poss)
    
# SUBSTITUTION METHODS

def gendigisub():
    mname = 'digsub_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [int(str(n)[:1] + \'\'.join(' + gendsubarr() + '[int(p)] for p in str(n)[1:])) for n in x]' 
   
def genasciisub():
    mname = 'asciisub_' + gentag()
    methods.append(mname)
    return 'def ' + mname + '(x):\n    return [int(\'\'.join(str(ord(f)) for f in str(n))) for n in x]'
    
ops = [genmul, genadd, gensub, genxor, 
       gencmul, gencadd, gencsub, gencxor, 
       genchmul, genchadd, genchsub, genchxor,
       genshuffle, genchunk, gendeck, gendigisub]
    
taunts = ['evil', 'encryption', 'lel', 'so good', 'kek', 'the best', 'mucho encrypto', 'the flag is flag{jk}', 'rekt', 'lmaooo', 'just reverse it', 'shiet?']    
    
out = open('mucho_encrypto.py', 'w')
out.write('flag = [ord(i) for i in \'' + flag + '\']\n')
out.write('k = len(flag)\n')
for i in range(5000):
    mth = random.choice(ops)() + '\n'
    if r(1, 100) < 50:
        mth = mth.replace('\n    ', '\n    # ' + random.choice(taunts) + '\n    ', 1)
    out.write(mth)
    
out.write('\n\n# heh, so evil\n\n\n')
for x in range(25000):
    out.write('flag = ' + random.choice(methods) + '(flag)\n')
    
out.write('\n\nflag = [str(j) for j in flag]\nopen("super_encrypted", "w").write("\\n".join(flag))\n')
out.close()


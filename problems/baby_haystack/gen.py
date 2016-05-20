import random, string
out = open('baby_haystack', 'a')
'''def rstr():
    return ''.join(random.choice(string.printable[:-2]) for i in xrange(random.randint))

for i in range(50):
    print i,
    out.write(rstr())
'''
for i in xrange(48755597):
    out.write(random.choice(string.printable[:-3]))
    
out.write('flag{all_haystacks_are_this_easy_right}')
print "\nWrote flag."

for i in xrange(64346445):
    out.write(random.choice(string.printable[:-3]))

print "\nDone."
out.close()

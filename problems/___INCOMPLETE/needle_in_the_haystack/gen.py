import random

flag = open("flag","r").readline()



def first_haystack():
    numchars = 100000000
    st = ""
    for i in xrange(numchars):
        if i % 100000 == 0:
            print i/200000000.
        c = random.randint(97, 97+26+1)
        st += chr(c)
    st += flag
    for i in xrange(numchars):
        if i % 100000 == 0:
            print (i+100000000)/200000000.
        c = random.randint(97, 97+26+1)
        st += chr(c)
    f = open("haystack1", "w")
    f.write(st)
    f.close()

first_haystack()
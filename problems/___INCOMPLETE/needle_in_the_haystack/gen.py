import random

flag = open("flag","r").readline()



def first_haystack():
    numchars = 100000000
    st = ""
    for i in xrange(numchars):
        c = random.randint(97, 97+26+1)
        st += chr(c)
    st += flag
    for i in xrange(numchars):
        c = random.randint(97, 97+26+1)
        st += chr(c)
    f = open("haystack1", "w")
    f.write(st)
    f.close()

first_haystack()
import random
flag = 'flag{i_liked_the_f1rst_on3_better_shouts_to_sctf}'
out = open('encrypted.dat', 'w')
for i in flag:
    f = ord(i)
    # generate number with bitlength equal to f
    k = 2**(f - 1) + random.randint(0, 2**(f - 1) - 1)
    # verify bitlength
    print chr(len(bin(k)[2:])),
    # write
    out.write(str(k) + '\n')

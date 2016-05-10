flag = 'flag{three_is_a_magic_numb3r_3333333}'
while len(flag) < 5 * 10**7:
    flag = flag.encode('hex')
open('several_threes.txt', 'w').write(flag)
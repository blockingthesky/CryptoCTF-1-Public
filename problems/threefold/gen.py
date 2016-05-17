flag = "flag{everything's_better_in_groups_of_three}"

while len(flag) < 5*10**7:
    flag = flag.encode('hex')
open('threefold', 'w').write(flag)
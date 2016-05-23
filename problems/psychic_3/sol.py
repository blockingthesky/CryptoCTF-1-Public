import os

files = len(os.walk("psychic3").next()[2])    

combs = [open('psychic3/psychic3_' + str(i) + '.lol', 'r').readline() for i in range(files)]
flag = ''
for i in range(len(combs[0])):
    nums = [int(u[i]) for u in combs]
    flag += chr(sum(nums))
print flag

import operator

flag = ''
for i in range(91):
    inp = open('psychic_2_files/psychic2_' + str(i) + '.lol', 'r').readline().decode('hex')
    inp = [ord(u) for u in inp]
    flag += chr(reduce(operator.xor, inp))
print flag
    

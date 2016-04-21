ctext = '110606521a1904010b155411101100010517024e571e151b001106065209021b0708451a49071c411545220b0b546b49390d412446170e4c26030e49154c1102090d001a07331852163a0603171757570f091a035c'
cipher = [int(ctext[2*i:2*i+2], 16) for i in range(len(ctext)/2)]
pad = [ord(j) for j in 'The ciphertext given was encrypted with a One Time Pad. It is perfectly secure. glhf!']
pt = ''
for m in range(len(cipher)):
    pt += chr(cipher[m]^pad[m])
print pt

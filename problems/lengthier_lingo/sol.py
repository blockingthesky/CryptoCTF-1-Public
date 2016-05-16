nums = [int(n.strip()) for n in open('encrypted.dat').readlines()]
print ''.join(chr(len(bin(k)[2:])) for k in nums)

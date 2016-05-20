def dsum(num):
    return sum(int(y) for y in num)

nums = [dsum(u.strip()) for u in open('maaaaaath.txt', 'r').readlines()]

flag = ''
for num in nums:
    for t in range(65, 127):
        if num % t == 0:
            flag += chr(t)

print flag

code = open('multi.pad', 'r').readline().decode('hex')
nums = {
    '1':'1',
    '2':'2ABCabc',
    '3':'3DEFdef',
    '4':'4GHIghi',
    '5':'5JKLjkl',
    '6':'6MNOmno',
    '7':'7PQRSpqrs',
    '8':'8TUVtuv',
    '9':'9WXYZwxyz',
    '0':'0'
}
dec = {}
for i in nums:
    for y in nums[i]:
        dec[y] = i

code = ''.join(dec[p] for p in code)
print code
nums = []
while len(code) != 0:
    if code[0] == '1':
        nums.append(int(''.join(code[:3])))
        code = code[3:]
    else:
        nums.append(int(''.join(code[:2])))
        code = code[2:]
#print nums
print ''.join(chr(t) for t in nums)

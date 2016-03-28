import math
nums = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def base(num, radix):
	st = math.ceil(math.log(num, radix))
	ret = ''
	while st >= 0:
		ret += nums[int(math.floor((num * 1.0)/(radix**st)))]
		num %= (radix**st)
		st -= 1
	return ret.lstrip('0')

flag = 'flag{the_sound_of_cryptographic_mystery}'
notes = [k for k in 'A B C# D E F# G#'.split()]

notout = open('notes.txt', 'w')

for m in flag:
    to = base(ord(m), 7)
    notto = ' '.join([notes[int(k)] for k in list(to)])
    notout.write(notto + '\n')

notout.close()

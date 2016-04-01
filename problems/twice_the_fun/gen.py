# double ASCII cipher
flag = 'flag{just_another_ASCII_cipher}'
ret = ''
for m in flag:
    ret += chr(ord(m) * 2)
open('message.txt', 'w').write(ret)

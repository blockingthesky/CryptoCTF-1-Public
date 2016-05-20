import random, string
#[^A-Za-z\.\?:!\',0-9]
chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.?:!', ")
def r():
    return ''.join(random.choice(string.printable[:-6] + '\n') for i in range(random.randint(100000, 150000)))
    
dct = {}
for i in chars:
    dct[i] = r()

out = open('dct.txt', 'w')
for i in chars:
    out.write(i + " ::::: " + dct[i] + "\n\n\t")

out.close()

msg = open('message.txt', 'r').readline().strip()
out = open('another_haystack', 'w')
for let in msg:
    out.write(dct[let])
out.close()


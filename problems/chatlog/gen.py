import random
messages = [[y.strip() for y in cur.strip().split(':')] for cur in open('chat.txt').readlines()]
ln = max(len(word[1]) for word in messages)
pad = [random.randint(0, 255) for i in range(100)]
for i in range(len(messages)):
    msg = messages[i][1]
    enc = [pad[p] ^ ord(msg[p]) for p in range(len(msg))]
    messages[i][1] = ''.join(hex(r)[2:] for r in enc)
out = open('chatpad.log', 'w')
out.write('[BEGIN CHAT LOG]\n')
out.write('\n\n'.join(': '.join(y) for y in messages))
out.write('\n[END CHAT LOG]')
out.close()
out = open('key', 'w')
out.write(str(pad) + '\n' + ''.join(hex(i)[2:] for i in pad))
out.close()
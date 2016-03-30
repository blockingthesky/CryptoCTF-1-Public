import math
msg = open('message.txt').readline()
box = int(math.sqrt(len(msg)))
for m in range(box):
    print ' '.join(msg[box*m : box*(m+1)])

msg = open('message.txt', 'r').readline()
print ''.join(chr(ord(m)/2) for m in msg)

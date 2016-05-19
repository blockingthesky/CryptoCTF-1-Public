c = open("fibcrypted.txt").read()
cm = [ord(x) for x in c]

while not c.startswith("flag{"):
    newChr = ord(c[0])-ord(c[1])
    if newChr<0:
        newChr+=128
    c+=chr(newChr)
    c=c[1:]

print c
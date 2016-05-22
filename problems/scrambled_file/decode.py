a = open('wut','rb')
data = a.read()
a.close()
#out = open('out','wb')
for byte in data:
    #print(hex(byte))
    #print(hex((byte+13)%0xff))
    print(hex((byte-13)%255).lstrip('0x').zfill(2),end='')
#out.close()

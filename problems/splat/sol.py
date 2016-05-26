import Image

pix = Image.open('splatter.png').load()

dct = {(255, 255, 255):' '}

nxt = 'a'

message = ''

for i in range(12):
    for j in range(25):
        squ = (255, 255, 255)
        for x in range(5):
            for y in range(5):
                if pix[5*i+x,5*j+y][:3] != (255, 255, 255):
                    squ = pix[5*i+x,5*j+y][:3]
        if squ not in dct:
            dct[squ] = nxt
            nxt = chr(ord(nxt) + 1)
        message += dct[squ]
print message
            
        

import Image, math

lin = open('den_so_wave.txt', 'r').readline()
size = int(math.sqrt(len(lin)))

img = Image.new('RGB', (size, size), 'white')
pix = img.load()

for r in range(size):
    for c in range(size):
        
        pix[r,c] = (0, 0, 0) if int(lin[150 * r + c]) == 1 else (255, 255, 255)

img.save('qrcode.out.png')

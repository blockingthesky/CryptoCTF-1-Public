import Image, random

# def splatter

img = Image.new('RGB', (60,125), 'white')
pix = img.load()
msg = "finding new ways to substitute things in for letters is first and foremost an excellent way to kill time but it is also great for trolling people in CTFs like this problem is trying to do to you hahahah get trolled mate flag brace straight substitution is for boring people brace yay for cryptography".lower()

alp = dict((t,(random.randint(0,255),random.randint(0,255),random.randint(0,255))) for t in 'abcdefghijklmnopqrstuvwxyz')
alp[' '] = (255, 255, 255)
open('ans.txt', 'w').write(str(alp))
for i in range(12):
    for j in range(25):
        for p in range(10):
            pix[5*i+random.randint(0,4),5*j+random.randint(0,4)] = alp[msg[25*i+j]]
img.save('splatter.png')

dt = {}
alp = list('abcdefghijklmnopqrstuvwxyz')

for k in 'bro dank kush memes 420 kek memes rekt fire xXx bongripz fresh stale urmom headshot 360noscope mlg newfag illuminati uwot m8 m9 yolo roflmfao hawt OP'.split():
    dt.update({alp.pop():k})

dt.update({' ':"BREAK"})

rkt = []

for k in 'What the trash did you just trashing say about me you little trash Ill have you know I graduated top of my class in the Navy Seals and Ive been involved in numerous secret raids on AlTrasha and I have over  confirmed kills I am trained in gorilla warfare and Im the top sniper in the entire US armed forces You are nothing to me but just another target I will wipe you the trash out with precision the likes of which has never been seen before on this Earth mark my trashing words You think you can get away with saying that trash to me over the Internet Think again trash As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm maggot The storm that wipes out the pathetic little thing you call your life Youre trashing dead kid I can be anywhere anytime and I can kill you in over seven hundred ways and thats just with my bare hands Not only am I extensively trained in unarmed combat but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable trash off the face of the continent you little trash If only you could have known what unholy retribution your little clever comment was about to bring down upon you maybe you would have held your trashing tongue But you couldnt you didnt and now youre paying the price you trashing idiot I will trash fury all over you and you will drown in it Youre trashing dead kiddo also the flag is leet smoked memes bro'.lower():
    rkt.append(dt.get(k))

out = open('mlg_crypto.txt', 'w')

out.write("===== BEGIN DANK ENCRYPTION BRO =====\n")

while len(rkt) != 0:
    linelen = 20 if len(rkt) >= 20 else len(rkt)
    pt = rkt[:linelen]
    rkt = rkt[linelen:]
    out.write('_'.join(pt) + "\n")

out.write("===== END DANK ENCRYPTION BRO =====")

out.close()

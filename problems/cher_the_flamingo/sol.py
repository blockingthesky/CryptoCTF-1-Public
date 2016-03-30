rhy = {
    'A' : 0,
    'B' : 1,
    'C#' : 2,
    'D' : 3,
    'E' : 4,
    'F#' : 5,
    'G#' : 6
    }

lin = open('notes.txt', 'r').readlines()
flag = ''
for mel in lin:
    mel = mel.strip().split()
    flag += chr(49 * rhy.get(mel[0]) + 7 * rhy.get(mel[1]) + rhy.get(mel[2]))

print flag
             

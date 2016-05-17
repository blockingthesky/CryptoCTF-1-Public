word = open('threefold', 'r').readline()
while '{' not in word:
    word = word.decode('hex')
print word
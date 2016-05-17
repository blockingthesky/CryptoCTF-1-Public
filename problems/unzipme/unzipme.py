import os, random

lol = [
        'almost_there', 'getting_close', 'you_can_do_it', 'just_a_few_more', 'i_believe_in_you', 'not_far_to_go',
        'honestly_not_that_bad', 'rip_ur_fingers', 'spaaaaaaaaaaaaaace', 'ez_just_unzip', 'winrar', 'flag',
        'theres_probably_something_in_here', 'lol', 'kek', 'cant_stump_the_trump'
       ]


os.popen('zip rip.zip flag.txt')
lastname = 'rip'
nextname = 'rip'

for i in xrange(10000):
    if i % 1000 == 0:
        print i/100,'%'
    # name the next zip
    while nextname == lastname:
        nextname = random.choice(lol)
    # zip the old file
    os.popen('zip ' + nextname + '.zip ' + lastname + '.zip')
    # remove the old file
    os.popen('rm ' + lastname + '.zip')
    lastname = nextname
    
os.popen('zip mordor.zip ' + lastname + '.zip')
    
# ssh jacob@45.55.199.182 tail -f /path/to/file | logstalgia --sync

import random

nums = {
    '1':'1',
    '2':'2ABCabc',
    '3':'3DEFdef',
    '4':'4GHIghi',
    '5':'5JKLjkl',
    '6':'6MNOmno',
    '7':'7PQRSpqrs',
    '8':'8TUVtuv',
    '9':'9WXYZwxyz',
    '0':'0'
}

message = ("The cryptrollgraphy problems in this competition seem to "
    "detract from it's image, as whoever keeps making them doesn't "
    "seem to take himself seriously. A phone pad? And in this format? "
    "It just doesn't seem right. This isn't even a one time pad. "
    "flag{7he_Harder_th3y_are}")

nms = list(''.join(str(r) for r in [ord(f) for f in message]))
open('multi.pad', 'w').write(''.join(random.choice(nums[p]) for p in nms).encode('hex'))


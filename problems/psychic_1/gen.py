import string, math

primes = filter(lambda x: not any(x % i == 0 for i in range(2,int(math.sqrt(x) + 1))), range(2,10000))

def rot(let, amt):
    if let not in string.ascii_letters:
        return let
    k = ord(let)
    if k > 96:
        k -= 97
        return chr((k + amt) % 26 + 97)
    k -= 65
    return chr((k + amt) % 26 + 65)

message = ("Sorry, sometimes problem statements are "
"difficult to come up with. This seemed like an easy "
"way out. The flag is flag{color_by_numbers_and_rot_"
"by_primes}")

open('decryptme', 'w').write(''.join(rot(message[i], primes[i]) for i in range(len(message))))

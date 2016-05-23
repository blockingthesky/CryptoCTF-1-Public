import string, math

primes = filter(lambda x: not any(x % i == 0 for i in range(2,int(math.sqrt(x) + 1))), range(2,10000))

def rot(let, amt):
    if let not in string.ascii_letters:
        return let
    k = ord(let)
    if k > 96:
        k -= 97
        return chr((k - amt) % 26 + 97)
    k -= 65
    return chr((k - amt) % 26 + 65)

ciphertext = open('decryptme', 'r').readline()

print ''.join(rot(ciphertext[i], primes[i]) for i in range(len(ciphertext)))

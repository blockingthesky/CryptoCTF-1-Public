message = "Encrypting the flag with the problem statement? That's low. flag{keys_are_everywhere}"
encrypt = "The ciphertext given was encrypted with a One Time Pad. It is perfectly secure. glhf!"

out = open('encrypted.txt', 'w')
out.write(''.join(hex(ord(message[i]) ^ ord(encrypt[i]))[2:].zfill(2) for i in range(len(message))))
out.close()

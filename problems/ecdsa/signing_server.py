#!/usr/bin/python

import socketserver as ss
import threading as th
from ecdsa import SigningKey, NIST384p

with open('flag.txt', 'r') as f:
    flag = f.read()
with open('ecdsa_signing_key.txt', 'r') as f:
    sk = SigningKey.from_string(f.read())

WELCOME_MSG = '''Welcome to my ECDSA signing server!

Please enter the message you wish to sign.
'''

class ecdsa_handler(ss.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes(WELCOME_MSG, 'ascii'))
        self.data = self.request.recv(1024).strip()
        self.request.sendall(bytes(
            'Signing message from {}... '.format(self.client_address[0]),
            'ascii'
        ))
        
        signature = sk.sign_deterministic(self.data).encode("hex")
        if signature == flag:
            self.request.sendall(b"Nice try, but I won't sign that for you!")
        else:
            self.request.sendall(bytes(
                "The signature is:\n\n{}\n\n".format(
                    signature
                ), 'ascii'
            ))
        self.request.close()

class ForkingTCPServer(ss.ForkingMixIn, ss.TCPServer):
    pass

if __name__ == '__main__':
    HOST, PORT = 'localhost', 4467
    ForkingTCPServer.allow_reuse_address = True
    server = ForkingTCPServer((HOST, PORT), ecdsa_handler)
    ip, port = server.server_address
    server.serve_forever()
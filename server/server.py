__author__ = 'bryanp'

import socket,shutil, os, hashlib, sys
from urllib2 import urlopen

class broadcast:

    def __init__(self):

        # make a mods folder if it doesn't exist
        try:
            os.mkdir('server/mods')
        except:
            pass

        self.s = socket.socket() # Create a socket object
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = ''
        self.port = 49491                          # Reserve a port for your service
        self.s.bind((self.host, self.port))        # Bind to the port

        # Get server public ip
        self.my_ip = urlopen('http://ip.42.pl/raw').read()
        print('Starting server on ' + self.my_ip + ' on port ' + str(self.port) + '\n')

        print('Compressing mods folder\n')
        shutil.make_archive('server/mods', 'zip', 'server/mods')

    # This function returns the hash value of a file
    def hash(self, blocksize=65536):

        hasher = hashlib.sha256()
        afile = open('server/mods.zip', 'rb')
        buf = afile.read(blocksize)

        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)

        afile.close()
        return hasher.digest()

    # This function broadcasts the server mods and hash to connected peers
    def broadcastML(self):

        self.s.listen(50)                           # Now wait for client connection
        self.f = open('server/mods.zip','rb')
        self.i = 0

        while True:
            self.c, self.addr = self.s.accept()     # Establish connection with client
            print 'Got connection from', self.addr

            l = self.f.read(1024)
            print 'Sending mod files to', self.addr
            while (l):
                self.c.send(l)
                self.i += 1
                print 'Uploading file mods.zip %dkb\r'%self.i,
                l = self.f.read(1024)
            self.f.close()
            print 'Done sending mods to', self.addr, '\n'

            self.c.close()                           # Close the connection

if __name__ == '__main__':

    server = broadcast()
    hash = server.hash()

    while True:

        print('Server is running\n')

        try:
            server.broadcastML()
            print('File sent\n')
            sys.exit()

        except:
            os.remove('server/mods.zip')
            print('Server shutdown unexpectedly\n')
            sys.exit()
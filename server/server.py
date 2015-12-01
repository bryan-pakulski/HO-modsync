__author__ = 'bryanp'

import socket,shutil, os, hashlib

class broadcast:

    def __init__(self):

        self.s = socket.socket()                   # Create a socket object
        self.host = socket.gethostname()           # Get local machine name
        self.port = 49491                          # Reserve a port for your service
        self.s.bind((self.host, self.port))        # Bind to the port

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

        self.s.listen(5)                           # Now wait for client connection
        self.f = open('server/mods.zip','rb')

        while True:
            self.c, self.addr = self.s.accept()     # Establish connection with client
            print 'Got connection from', self.addr

            l = self.f.read(1024)
            while (l):
                print 'Sending mod files to', self.addr
                self.c.send(l)
                l = self.f.read(1024)
            self.f.close()
            print 'Done sending mods to', self.addr, '\n'

            self.c.close()                          # Close the connection

if __name__ == '__main__':

    server = broadcast()
    hash = server.hash()

    print('server is running\n')

    try:
        server.broadcastML()
        print('File sent\n')

    except:
        os.remove('server/mods.zip')
        print('Server shutdown unexpectedly\n')
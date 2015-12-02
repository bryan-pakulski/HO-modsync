__author__ = 'bryanp'

import socket,shutil, os, sys

# Server class, sends data
class broadcast:

    def __init__(self):

        # make a mods folder if it doesn't exist
        try:
            os.mkdir('mods')
        except:
            pass

        # Create a socket object and make it be able to reuse an old address that hasn't been cleaned yet
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = ''
        # Port the server broadcasts on
        self.port = 49491
        self.s.bind((self.host, self.port))

        print('Starting server on port ' + str(self.port) + '\nRemember to forward this port!\n')

        print('Compressing mods folder\n')
        # Compress the contents of the mods folder into a zip file called mods.zip
        shutil.make_archive('mods', 'zip', 'mods')

    # This function broadcasts the server mods to connected clients
    def broadcastML(self):

        # Listen for a maximum of 32 connections
        # (more than any we should have on a given map but this at least allows for expansion)
        self.s.listen(32)

        # Broadcast the mods.zip file until interupted
        while True:

            self.f = open('mods.zip','rb')
            self.i = 0

            # Establish connection with client
            self.c, self.addr = self.s.accept()
            print 'Got connection from', self.addr

            l = self.f.read(256)
            print 'Sending mod files to', self.addr
            # Send data to client in 256 byte chunks
            while (l):
                self.c.send(l)
                self.i += 1
                print('Uploading file mods.zip %d kb\r'%self.i),
                l = self.f.read(256)
            self.f.close()
            print 'Done sending mods to', self.addr, '\n'

            # Close the connection
            self.c.close()

# Run the program and handle possible exceptions
if __name__ == '__main__':

    # Create instance of a server
    server = broadcast()

    while True:

        print('Server is running\n')

        try:
            server.broadcastML()
            print('File sent\n')
            sys.exit()

        except:
            try:
                os.remove('mods.zip')
                print('Program closed successfully\n')
                sys.exit()
            except:
                print('An error occured deleting the mods.zip file, may have to be removed manually, shutting down')
                sys.exit()
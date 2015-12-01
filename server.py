__author__ = 'bryanp'

import socket

class broadcast:

    def __init__(self):

        self.s = socket.socket()                   # Create a socket object
        self.host = socket.gethostname()           # Get local machine name
        self.port = 49491                          # Reserve a port for your service
        self.s.bind((self.host, self.port))        # Bind to the port

    # This function broadcasts the server modlist and hashes to connected peers
    def broadcastML(self):

        self.s.listen(5)                           # Now wait for client connection

        while True:
            self.c, self.addr = self.s.accept()     # Establish connection with client
            print 'Got connection from', self.addr
            self.c.send('Connected to host\n')
            self.c.send('Recieving master list of server mods')
            self.c.close()                          # Close the connection




def main():
    server = broadcast()
    print("server is running\n")
    server.broadcastML()

if __name__ == "__main__":
    main()
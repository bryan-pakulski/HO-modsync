__author__ = 'bryanp'

import socket, zipfile, os, sys, shutil, select


# Client class, recieves data
class recieve:

    def __init__(self):

        # Check if ip file exists, if not create it
        if os.path.isfile('ip') == False:
            self.ip = open('ip', 'w+')
            self.ip.close()

        # Delete all old mods
        try:
            shutil.rmtree('mods')
            os.mkdir('mods')
        except:
            os.mkdir('mods')

        # Create a socket object and make it be able to reuse an old address that hasn't been cleaned yet
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Server ip is read from a file, that way only some code has to be added to the eldorito interface to place
        # server ip into this file
        self.ip = open('ip', 'r')

        self.host = self.ip.readline()
        self.ip.close()
        # Port used by the client to recieve data
        self.port = 49491

    # This function recieves data from the server and stores it in a zip folder
    def recieveML(self):

        # Create our empty zip folder
        self.f = open('mods.zip','wb')
        self.i = 0 # Size counter for our file

        # Attempt to connect to the server
        try:
            self.s.connect((self.host, self.port))
        except:
            print("Couldn't connect to server, quitting")
            sys.exit()

        # Here the program begins to recieve data from the server in 1024 byte chunks
        print('Recieving server mods\n')
        l = self.s.recv(1024)

        while (l):
            # Write data to our zip file
            self.f.write(l)

            self.s.setblocking(0)
            # This check makes sure we have valid data to write
            ready = select.select([self.s], [], [], 5)
            if ready[0]:
                l = self.s.recv(1024)

            self.i += 1 # Increment our data size counter and print the result
            print ('Downloading file mods.zip %d kb\r'%self.i),
        self.f.close()

        # Close the socket when done
        self.s.close()

    # This function extracts our mods.zip folder into the mods directory
    def extractmods(self):

        print('Extracting server mods\n')
        with zipfile.ZipFile('mods.zip', "r") as z:
            z.extractall('mods')

# Run the program and handle possible exceptions
if __name__ == "__main__":
    try:

        # Create an instance of the client class and download and extract the mods
        client = recieve()
        client.recieveML()
        client.extractmods()


        print("Server mods recieved\n")
        sys.exit()
    except:
        try:
            os.remove('mods.zip')
            print('Program closed successfully\n')
            sys.exit()
        except:
            print('An error occured deleting the mods.zip file, may have to be removed manually, shutting down')
            sys.exit()
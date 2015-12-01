__author__ = 'bryanp'

import hashlib, socket, zipfile, os, sys, shutil, select


class recieve:

    def __init__(self):

        # Delete all old mods
        try:
            shutil.rmtree('mods')
            os.mkdir('mods')
        except:
            os.mkdir('mods')

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Server ip is read from a text file, that way only some code has to be added to the eldorito interface to place
        # server ip into this text file
        self.ip = open('ip.txt', 'w+')

        self.host = self.ip.readline()
        self.ip.close()
        self.port = 49491 # Reserve a port for your service.

    def recieveML(self):

        self.f = open('mods.zip','w+')
        self.i = 0

        try:
            self.s.connect((self.host, self.port))
        except:
            print("Couldn't connect to server, quitting")
            sys.exit()

        print('Recieving server mods\n')
        l = self.s.recv(1024)
        while (l):
            self.f.write(l)

            self.s.setblocking(0)
            ready = select.select([self.s], [], [], 5)
            if ready[0]:
                l = self.s.recv(1024)

            self.i += 1
            print ('Downloading file mods.zip %d kb\r'%self.i),
        self.f.close()

        self.s.close()                       # Close the socket when done

    def extractmods(self):

        print('Extracting server mods\n')
        with zipfile.ZipFile('mods.zip', "r") as z:
            z.extractall('mods')


# Main function
def main():

    client = recieve()
    client.recieveML()
    client.extractmods()


# Run the program
if __name__ == "__main__":
    try:
        main()
        print("Server mods recieved\n")
        sys.exit()
    except:
        os.remove('mods.zip')
        sys.exit()
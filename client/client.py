__author__ = 'bryanp'

import hashlib, socket, zipfile, os, sys, shutil


class recieve:

    def __init__(self):

        # Delete all old mods
        try:
            shutil.rmtree('client/mods')
            os.mkdir('client/mods')
        except:
            os.mkdir('client/mods')

        self.s = socket.socket()         # Create a socket object
        self.host = socket.gethostname() # Get local machine name
        self.port = 49491                # Reserve a port for your service.


    # This function returns the hash value of a file
    def hash(self, blocksize=65536):

        hasher = hashlib.sha256()
        afile = open('client/mods.zip', 'rb')
        buf = afile.read(blocksize)

        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)

        return hasher.digest()


    def recieveML(self):

        self.f = open('client/mods.zip','w+')

        try:
            self.s.connect((self.host, self.port))
        except:
            print("Couldn't connect to server, quitting")
            sys.exit()

        print('Recieving server mods\n')
        l = self.s.recv(1024)
        while (l):
            self.f.write(l)
            l = self.s.recv(1024)
        self.f.close()

        self.s.close                     # Close the socket when done


    def checkhash(self):

        self.Dhash = hash()
        self.Ohash = 12 #TODO get original hash from server


    def extractmods(self):

        print('Extracting server mods\n')
        with zipfile.ZipFile('client/mods.zip', "r") as z:
            z.extractall('client/mods')


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
        os.remove('client/mods.zip')
    except:
        os.remove('client/mods.zip')
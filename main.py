__author__ = 'bryanp'

import hashlib, os, socket, thread


# This function returns the hash value of a file
def hashfile(afile, hasher, blocksize=65536):

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    return hasher.digest()


# This function is used to create the mods directory and the mods list file
def moddir():

    if not os.path.exists("mods"):
        print("Mod directory doesn't exist, creating folder\n")
        os.makedirs("mods")
        os.mkfifo("mods/modlist.json")

    else:
        print("Mod directory exists\n")


# This function adds mods to the mod list file, it adds the mod name and details to a json file
def addmod(name):

    #TODO add code that will use a special mod format i.e. a json file inside a mod directory that contains mod details
    pass

class recieve:

    def __init__(self):
        self.s = socket.socket()         # Create a socket object
        self.host = socket.gethostname() # Get local machine name
        self.port = 49491                # Reserve a port for your service.

    # This function recieves the server modlist and hashes (called by peers)
    # This function will need to recieve a C hook inside the main function in order to get the ip addresses needed
    def recieveML(self):

        self.s.connect((self.host, self.port))

        print self.s.recv(2048)

        self.s.shutdown                     # Close the socket when done

# Main function
def main():

    moddir()

    client = recieve()
    client.recieveML()


# Run the program
if __name__ == "__main__":
    main()
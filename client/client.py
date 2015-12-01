__author__ = 'bryanp'

import hashlib, os, socket, thread

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

    client = recieve()
    client.recieveML()


# Run the program
if __name__ == "__main__":
    main()
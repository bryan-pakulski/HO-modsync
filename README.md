# HO-modhash
A python application being designed for halo online. It's purpose is to be run on a server where it will make sure all users have the same mods as each other and if not download them from the server host.

# How to use it
For now the synchronisation has to be done through a text file that is changed by eldorito server browser (by filling in the chosen server ip) that will allow the client to connect to the server ip
Also the port 49491 MUST be forwarded for this program to work!

##### Server
Place mods into the mod folder with the server executable (if it's not there run the program once for it to generate and then close) and then just run the server.

##### Client
As for clients for now you have to manually connect to the server ip, but once input it will download all the server mods and extract them into the client mod folder

# NOTE:
All the folders and such will be generated on runtime, don't worry if they aren't there initially

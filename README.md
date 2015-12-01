# HO-modhash
A python application being designed for halo online. It's purpose is to be run on a server where it will make sure all users have the same mods as each other and if not download them from the server host. It will need C++ or C hooks in order it to be called by a client (i.e use server host ip as input for the client side code in order to download the mods the server is running)

# How to use it
For now the synchronisation has to be done through C++ or C hooks that will allow the client to connect to the server ip
Also the port 49491 MUST be forwarded for this program to work

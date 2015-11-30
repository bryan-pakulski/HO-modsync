__author__ = 'bryanp'

import hashlib, os


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
        os.mknod("modlist.txt")

    else:
        print("Mod directory exists\n")

# This function adds mods to the mod list file
def addmod(name):

    #TODO add code that will use a special mod format i.e. a json file in a mod directory that contains mod details
    pass

# Main function
def main():

    moddir()

# Run the progra
if __name__ == "__main__":
    main()
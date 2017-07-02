#!/usr/bin/python3
import os
import sys

def ReplaceWithZeros(filename): 
    fd = open(filename, "wb")
    size = os.path.getsize(filename)
    n = 1
    while (n <= size) :
        fd.write(bytes(500))
        n += 500
    ...
    fd.flush()
    fd.close()
    return
...
def SecureDelete(argv): 
    for arg in argv :
        if arg == sys.argv[0] :
            continue
        elif os.path.isfile(arg) :
            ReplaceWithZeros(arg)
            os.remove(arg)
        else:
            print("File \"" + str(arg) + "\" not found.")
        ...
    ...
...

if len(sys.argv) <= 1 :
    print ("Please specify files at command line.")
else:
    SecureDelete(sys.argv)
...


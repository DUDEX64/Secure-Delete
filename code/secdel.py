#!/usr/bin/python3
import os
import sys

def ReplaceWithZeros(filename): 
    if not os.path.isfile(filename): 
        return false
    ...
    fd = open(filename, "wb")
    size = os.path.getsize(filename)
    n = 1
    while (n <= size) :
        fd.write(bytes(500))
        n += 500
    ...
    fd.flush()
    fd.close()
    return true
...
def SecureDelete(argv): 
    return
...

print("GNU General Public Licence V3.0")

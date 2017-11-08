'''
Karnauch, Andrey
CS483 - IO module
Processes input arguments using argparse
'''

import sys
import binascii
import argparse

parser = argparse.ArgumentParser(description='Encrypt/Decrypt an RSA integer')
parser.add_argument("-k", dest="key_file",help="Key file generated using rsa-gen") 
parser.add_argument("-i", dest="input_file",help="File with base10 int that is being operated on")
parser.add_argument("-o", dest="output_file",help="File where resulting output is stored in base10")

args = parser.parse_args()

if (args.key_file == None):
    print("Must include a key file", file=sys.stderr)
    print("Rerun using '-h' for help", file=sys.stderr)
    sys.exit()
elif (args.input_file == None):
    print("Must include an input file", file=sys.stderr)
    print("Rerun using '-h' for help", file=sys.stderr)
    sys.exit()
elif (args.output_file == None):
    print("Must include an output file", file=sys.stderr)
    print("Rerun using '-h' for help", file=sys.stderr)
    sys.exit()

'''
Reads key in from the file provided via command line arguments
@return: returns the hex encoded string as a byte string
def getKey():
    with open(args.key_file, "rb") as k:
        key = k.read()
        key = binascii.unhexlify(key)
        return key
'''
'''
Reads input in from the file provided via command line arguments
@return: returns the byte string
'''
def getKey():
    with open(args.key_file, "r") as f:
        three_lines = f.read()

    split = three_lines.splitlines()
    nbits = split[0]
    n = split[1]
    key = split[2]
    return nbits, n, key

def getInput():
    with open(args.input_file, "r") as f:
        s = f.read()
        return s.splitlines()[0]

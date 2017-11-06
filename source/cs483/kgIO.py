'''
Karnauch, Andrey
CS483 - IO module
Processes input arguments using argparse for key-gen.py
'''

import sys
import binascii
import argparse

parser = argparse.ArgumentParser(description='Generate an RSA key')
parser.add_argument("-p", dest="public_key",help="File to store public key")
parser.add_argument("-s", dest="private_key",help="File to store private key")
parser.add_argument("-n", dest="num_bits",help="Specifies number of bits in your N")

args = parser.parse_args()

if (args.public_key == None):
    print("Must output a public key file", file=sys.stderr)
    print("Rerun using '-h' for help", file=sys.stderr)
    sys.exit()
elif (args.private_key == None):
    print("Must output a private key file", file=sys.stderr)
    print("Rerun using '-h' for help", file=sys.stderr)
    sys.exit()
elif (args.num_bits == None):
    print("Must specify number of bits in N", file=sys.stderr)
    print("Rerun using '-h' for help", file=sys.stderr)
    sys.exit()

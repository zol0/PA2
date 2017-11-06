'''
Karnauch, Andrey
CS483 - cbc_enc.py
Encrypts a message using AES CBC mode with own padding
'''

from cs483 import AESHelper
from cs483 import IO
from Crypto import Random

BSIZE = 16

'''
Encrypts string
@param a: an AESHelper object that calls AES ECB functions
@param plain: a byte string of plaintext that is already padded
@param iv: Initialization vector generated randomly or provided by user
@return: a byte string that is padded and fully encrypted 
'''
def cbcenc(a,plain,iv):

    pXORiv = a.xor(plain[:16],iv)
    finalCipher = iv
    i = BSIZE;

    cipher = a.encrypt(pXORiv)

    finalCipher += cipher

    while (i < len(plain)):
        pXORiv = a.xor(plain[i:i+BSIZE],cipher)
        cipher = a.encrypt(pXORiv)
        finalCipher += cipher
        i += BSIZE

    return finalCipher

if __name__ == "__main__": #Processes input, pads, encrypts, and prints to file

    key = IO.getKey()
    msg = IO.getInput()

    a = AESHelper(key)

    iv = IO.getIV()
    if (iv == None):
        iv = Random.new().read(BSIZE)

    pad_msg = a.pad(msg)
    result = cbcenc(a, pad_msg, iv)

    with open(IO.args.output_file, "wb") as w:
        w.write(result)


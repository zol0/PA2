'''
Karnauch, Andrey
CS483 - ctr_enc.py
Encrypts text using AES CTR mode in parallel
'''

import sys
from itertools import repeat
from multiprocessing import Pool, cpu_count
from cs483 import AESHelper
from cs483 import IO
from Crypto import Random

BSIZE = 16

'''
Encrypts (and decrypts) byte string
@param a: an AESHelper object that does AES ECB processing
@param iv: a byte string whose length is equal to the block length
@param text: a single BLOCK of a byte string
@return: a single block of ciphertext/plaintext
'''
def ctr_encrypt(a,iv,text):
    encrypted = a.encrypt(iv)
    cipher = a.xor(text,encrypted)
    return cipher

'''
Increments the CTR(IV) by 1
@param iv: a byte string
@return: a byte string (iv+1)
'''
def increment_iv(iv):
    iv_int = (int.from_bytes(iv, sys.byteorder))+1
    return iv_int.to_bytes(len(iv), sys.byteorder)

if __name__ == "__main__":

    key = IO.getKey()
    msg = IO.getInput()
    iv = IO.getIV()

    if (iv == None): iv = Random.new().read(BSIZE)
    orig_iv = iv

    a = AESHelper(key)

    all_ivs = []
    msg_in_blocks = []
    msg_in_blocks.append(msg[:BSIZE])
    all_ivs.append(iv)

    i = BSIZE

    '''
    Sets up the input for parallel processing
    Calculates all values of the IV + CTR we will need
    Breaks the message into all appropriate block sizes
    '''
    while (i < len(msg)):
        iv = increment_iv(iv)
        all_ivs.append(iv)
        msg_in_blocks.append(msg[i:i+BSIZE])
        i += BSIZE

    '''
    Pool of workers created based on CPUs available
    Each worker is assigned personal inputs to the ctr_encrypt function
    Workers increment through provided data structures to perform encryption
    '''
    pool = Pool(cpu_count())
    finalCipher = pool.starmap(ctr_encrypt, zip(repeat(a), all_ivs, msg_in_blocks))
    finalCipher.insert(0, orig_iv) #Prepends the original IV used to the front
    finalCipher = b''.join(finalCipher)

    with open(IO.args.output_file, "wb") as w:
        w.write(finalCipher)

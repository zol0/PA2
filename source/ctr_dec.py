'''
Karnauch, Andrey
CS483 - ctr_dec.py
Decrypts text using AES CTR mode in parallel
'''

import sys
from itertools import repeat
from multiprocessing import Pool, cpu_count
from cs483 import AESHelper
from cs483 import IO

#uses modules from ctr_enc to perform same exact tasks for decryption
#see ctr_enc.py for more details
from ctr_enc import ctr_encrypt, increment_iv

BSIZE = 16

if __name__ == "__main__":

    key = IO.getKey()
    msg = IO.getInput()
    
    a = AESHelper(key)

    iv = msg[:16]

    all_ivs = []
    all_ivs.append(iv)
    msg_in_blocks = []

    i = BSIZE

    while (i < len(msg)):
        iv = increment_iv(iv)
        all_ivs.append(iv)
        msg_in_blocks.append(msg[i:i+BSIZE])
        i += BSIZE

    pool = Pool(cpu_count())
    finalCipher = pool.starmap(ctr_encrypt, zip(repeat(a), all_ivs, msg_in_blocks))
    finalCipher = b''.join(finalCipher)

    with open(IO.args.output_file, "wb") as w:
        w.write(finalCipher)

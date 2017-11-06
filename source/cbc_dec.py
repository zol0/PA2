'''
Karnauch, Andrey
CS483 - cbc_dec.py
Decrypts using AES CBC mode with own padding
'''
from cs483 import AESHelper
from cs483 import IO

BSIZE = 16

'''
Decrypts message
@param a: an AESHelper object to access AES ECB functions
@param msg: the result of cbc-enc
@return: a decrypted byte string with padding of cbc-enc still appended
'''
def cbcdec(a,msg):
    iv = msg[:BSIZE]
    i = BSIZE
    decMsg = b''

    while (i < len(msg)):
        text = a.decrypt(msg[i:i+BSIZE])
        decMsg += a.xor(text,iv)
        iv = msg[i:i+BSIZE]
        i += BSIZE
    
    return decMsg

if __name__ == "__main__": #Processes input, decrypts, unpads, and prints to a file

    key = IO.getKey()
    msg = IO.getInput()

    a = AESHelper(key)

    plain = cbcdec(a,msg)
    final_message = a.unpad(plain)

    with open(IO.args.output_file, "wb") as w:
        w.write(final_message)

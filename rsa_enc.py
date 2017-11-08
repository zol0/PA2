from source.cs483 import rsaIO
import random
import sys
import os

def genRandom(r):
    rbytes = r // 8
    print("Need", r, "random bits ")
    print("Need", rbytes, "random bytes ")
    padr = b''
    while (len(padr) < rbytes):
        num_zeros = rbytes - len(padr)
        get_bytes = os.urandom(num_zeros)
        if (get_bytes.find(b'\x00') != -1): print("Found zeros in", get_bytes)
        get_bytes = get_bytes.replace(b'\x00', b'')
        padr = padr + get_bytes

    print("Got", len(padr), "bytes")
    print("padding = ", padr)
    return padr

def pad(m, nbits, n):
    r = nbits // 2
    max_length = r - 24

    rbytes = r // 8
    mbytes = m.bit_length() // 8

    left_over = r - (rbytes*8)
    if (m.bit_length() > max_length): 
        print('**ERROR**\n',
        'Bits in N = %d\n' % nbits,
        'Bits in R = %d\n' % r,
        'Bits in message = %d\n' % m.bit_length(),
        'Total = %d + %d + 24 = %d\n'
        % (r, m.bit_length(), 24+r+m.bit_length()),
        'Message too large!')
        exit(1)

    need = max_length - m.bit_length() + left_over
    num_zeros = need // 8

    zero_string = bytearray(num_zeros)
    print("Created zero string ", zero_string)

    padding = genRandom(r)
    return b'\x00' + b'\x02' + padding + b'\x00' + zero_string + m.to_bytes((m.bit_length() // 8)+1, sys.byteorder)

def enc(nbits, n, key, m):
    rv = pad(m, nbits, n)
    print("Returned", rv)
    print("RV length", len(rv))


if __name__ == "__main__":
    m = rsaIO.getInput()
    nbits, n, key = rsaIO.getKey()
#    print(m)
#    print("nbits = ", nbits)
#    print("n = ", n)
#    print("key = ", key)

    enc(int(nbits), int(n), key, int(m))



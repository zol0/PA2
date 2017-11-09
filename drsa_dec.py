from source.cs483 import rsaIO
import random
import math
import sys
import os

def dec(nbits, n, key, m):
    m_inv = pow(m, key, n)
    m_dec = m_inv.to_bytes((nbits // 8), sys.byteorder)
    print("Dec msg =", m_dec)
    if (m_dec[:2] != b'\x00\x02'):
        print("ERROR: Expected", b'\x00\x02', "as first two bytes", file=sys.stderr)
        print("Received", m_dec[:2], "instead!", file=sys.stderr)
        exit(1)
    
    strip_amount = 3 + (nbits//2//8)
    m_stripped = m_dec[strip_amount:]
    m_stripped = m_stripped.lstrip(b'\x00')
    print(m_stripped)
    m_plain = int.from_bytes(m_stripped, sys.byteorder)
    print("Message is", m_plain)
    return m_plain


if __name__ == "__main__":
    m = rsaIO.getInput()
    nbits, n, key = rsaIO.getKey()
    m_dec = dec(int(nbits), int(n), int(key), int(m))

    with open(rsaIO.args.output_file, "w") as w:
        w.write(str(m_dec))


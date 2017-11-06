import binascii
from source.cs483 import kgIO
from Crypto.Util import number
from math import gcd

def modInv(e, phi):
    prevx, y = 1, 1
    prevy, x = 0, 0
    orderN = phi

    while phi:
        q = e // phi
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        e, phi = phi, e % phi

    return prevx % orderN

def genE(orderN):
    for e in range(3, orderN, 2):
        if (gcd(e, orderN) == 1):
            return e

def genPublic(bits):
    p = number.getPrime(int(bits/2))
    q = number.getPrime(int(bits/2))
    N = p*q
    while (N.bit_length() != bits):
        q = number.getPrime(int(bits/2))
        N = p*q
    
    orderN = (p-1)*(q-1)
    e = genE(orderN)
    d = modInv(e, orderN)

    print("Found e = ", e)
    print("Inverse d = ", d)
    print("order = ", orderN)
    print("N = ", N)
    print("N = ", hex(p*q))
    print("len = ", N.bit_length())

    return N, e, d

def writeFile(name, N, key):
    with open(name, "w") as w:
        w.write(str(N.bit_length()) + "\n")
        w.write(str(N) + "\n")
        w.write(str(key) + "\n")

if __name__ == "__main__":
    bits = int(kgIO.args.num_bits)
    N, e, d = genPublic(bits)
    writeFile(kgIO.args.public_key, N, e)
    writeFile(kgIO.args.private_key, N, d)

from source.cs483 import rsaIO
from bitstring import BitArray, BitStream

def pad(m, nbits, n):
    r = nbits // 2
    max_length = r - 24
    if (int(m).bit_length() > max_length): 
        print("Error, m too big")
    else:
        i = 0
        m = int(m)
        need = max_length - m.bit_length()
        print("need =", need)
        a = BitArray(bin(m))
        while (i < need):
            a.prepend('0b0')
            i += 1

        print(a.bin)
        print(a.uint)
        print(a.bytes)
        print(len(a))

def enc(nbits, n, key, m):
    pad(m, nbits, n)


if __name__ == "__main__":
    m = rsaIO.getInput()
    nbits, n, key = rsaIO.getKey()
    print(m)
    print("nbits = ", nbits)
    print("n = ", n)
    print("key = ", key)

    enc(int(nbits), int(n), key, m)



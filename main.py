from base64 import b64encode, b64decode
import random
import sys

def single_byte_xor(message, key, encrypt=True):
    random.seed(key)
    if encrypt:
        bs = bytearray(message, encoding='ASCII')
    else:
        bs = bytearray(b64decode(message))

    n = len(bs)
    xor_bytes = random.randbytes(n)
    ba = bytearray()
    for b, k in zip(bs, xor_bytes):
        ba.append(b^k)

    if encrypt:
        encoded = b64encode(ba)
        encoded = encoded.decode('utf-8')
        return str(encoded)
    else:
        decoded = ba.decode("ASCII")
        return str(decoded)

def main():
    mode = input("Mode? Encrypt (E) or decrypt (D)\n")
    if mode == "E":
        message = input("What is message?\n")
        key = input("What is key?\n")
        key = int(key)
        print(single_byte_xor(message, key))
    elif mode == "D":
        userinput = input("What is the string to decrypt?\n")
        key = input("What is key?\n")
        key = int(key)
        print(single_byte_xor(userinput, key, encrypt=False))
    elif mode == "exit":
        sys.exit(1)
    else:
        print("idot\n")

if __name__ == "__main__":
    while True:
        main()
import string, sys

def vigenere_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Vigenere Cipher with a given key.
    """
    plaintext = ""
    key_len = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % key_len]
        if char.isupper():
            plaintext += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
        elif char.islower():
            plaintext += chr((ord(char) - ord(key_char) + 26) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python3 Challenge\ 07\ -\ XORians\- Gate.py <DECODED_XOR_KEY>")
        exit(1)
    key = sys.argv[1]
    ciphertext = "HKAU{Ytoa fgbrn gup unlq baympjk, ziddvv.}"
    decoded = vigenere_decrypt(ciphertext, key)
    print(decoded)

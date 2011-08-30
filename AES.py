#!/usr/bin/env python

class AES():
    def __init__(self, master_key):
        self.change_key(master_key)

    def change_key(self, master_key):
        return 0

    def encrypt(self, plaintext):
        return 0

    def decrypt(self, ciphertext):
        return 0


if __name__ == '__main__':
    plaintext = 0x3243f6a8885a308d313198a2e0370734
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    # the ciphertext should be
    # 0x3925841d02dc09fbdc118597196a0b32

    my_AES = AES(master_key)

    encrypted = my_AES.encrypt(plaintext)
    decrypted = my_AES.decrypt(encrypted)

    print 'plaintext:', hex(plaintext)
    print 'masterkey:', hex(master_key)

    print 'encrypted:', hex(encrypted)
    print 'decrypted:', hex(decrypted)
    

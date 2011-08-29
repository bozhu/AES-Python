#!/usr/bin/env python

def set_key(master_key):
    return 0

def encrypt(plaintext, round_keys):
    return 0

def decrypt(ciphertext, round_keys):
    return 0


if __name__ == '__main__':
    plaintext = 0x3243f6a8885a308d313198a2e0370734
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    # the ciphertext should be
    # 0x3925841d02dc09fbdc118597196a0b32

    round_keys = set_key(master_key)

    encrypted = encrypt(plaintext, round_keys)
    decrypted = decrypt(encrypted, round_keys)

    print 'plaintext:', hex(plaintext)
    print 'master key:', hex(master_key)

    print 'encrypted:', hex(encrypted)
    print 'decrypted:', hex(decrypted)
    

#!/usr/bin/env python3

import base64
from datetime import datetime


def debug(b): 
    a = '\x2e\x6c\x6f\x67'  #.log
    with open(a, 'a') as a: #appending
        a.write('# {} {} \n'.format(datetime.now(), b))


def encrypt(e):
    b = 0xABD79CC494212625 #12382538068591191589
    c = '101010101A4'
    for i in e:
        debug(str(b))                          # <- For Debug, REMOVE in Production.
        b = b ^ ord(str(i)) * int(c, 16)
    b ^= 0xABCDEFFEDCBAABC #0xABCDEFFEDCBAABC
    d = str.encode(hex(b)[2:])
    return base64.b64encode(d).decode()


def main():
    e = input('[+]Enter your password: ')
    f = encrypt(e)
    print('[+]Your encrypted password is: {}'.format(f))
    print('[+]Password has been saved to encrypted.txt')
    with open('encrypted.txt', 'w') as g:
        g.write(f)


if __name__ == '__main__':
    main()

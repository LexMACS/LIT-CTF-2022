from Crypto.Util.number import getPrime,isPrime
import random
import math
import cmath

from pwn import *;

from functools import reduce

def testRoots(n):
	m = n ** 2 + 1;
	return (m % 4 != 0 and isPrime(m));

# p1 = (10000000000000**4 - 1) // (10000000000000 - 1)
# p2 = (10000000000004**4 - 1) // (10000000000004 - 1)
# p3 = (10000000000008**4 - 1) // (10000000000008 - 1)

cnt = 10000000000000000;
while(True):
	if(testRoots(cnt)):
		print("FOUND " + str(cnt));
	cnt += 1;
# l1 = ((tryHash(10000000000000,p1)))
# print(p1 % 4);
# l2 = ((tryHash(10000001,p2)))
# l3 = ((tryHash(10000002,p3)))
# print(bytes.fromhex(hex(chinese_remainder([p1,p2,p3],[l1,l2,l3]))[2:]))

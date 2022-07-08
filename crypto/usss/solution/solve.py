from Crypto.Util.number import getPrime
import random
import math
import cmath

from pwn import *;

from functools import reduce

def chinese_remainder(n, a):
    tot = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        tot += a_i * mul_inv(p, n_i) * p
    return tot % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

p1 = (10000000000000017**3 - 1) // (10000000000000017 - 1)
p2 = (10000000000000076**3 - 1) // (10000000000000076 - 1)
p3 = (10000000000000092**3 - 1) // (10000000000000092 - 1)


def askHash(conn,a,po):
	print(conn.recv());
	conn.sendline(str(po));
	print(conn.recv());
	conn.sendline(str(a));
	res = int(conn.recvline().decode("utf-8").split(" ")[-1].strip())
	return res;
	# return c

def tryHash(b,p):
	assert(p % 3 != 0);
	listOfMods = [];
	while True:
		# assert(p == (b + 1) * (b * b + 1))
		assert(pow(2,p - 1,p) == 1);
		conn = remote('0.0.0.0',31337);
		print(conn.recvline());
		print(conn.recv());
		conn.sendline(str(p));
		power = int(conn.recvline().decode("utf-8").split(" ")[-1].strip());

		# FAIL
		phi = p - 1;
		if math.gcd(phi,power) != 1:
			continue;

		# 16% chance this will work, so we need about 6 tries
		negpower = mul_inv(power,phi);

		# assert(power * negpower % phi == 1);
		# print("WHAT " +  str(negpower));
		tot = askHash(conn,b**0,negpower);
		tot += askHash(conn,b**1,negpower) * (b ** 2);
		tot += askHash(conn,b**2,negpower) * (b ** 1);
		assert(p % 3 != 0);
		tot = tot * mul_inv(3,p) % p;
		tot %= p;
		if(tot in listOfMods):
			return tot;
		print(str(len(listOfMods)) + " " + str(tot));
		listOfMods.append(tot);

l1 = ((tryHash(10000000000000017,p1)))
l2 = ((tryHash(10000000000000076,p2)))
l3 = ((tryHash(10000000000000092,p3)))
print(bytes.fromhex(hex(chinese_remainder([p1,p2,p3],[l1,l2,l3]))[2:]))

import random
from sympy import *
from Crypto.Util.number import *

from pwn import *;

from functools import reduce


# Clients these days just keeping changing their requirements!
# Ill just let them choose whatever they want

flag = b"tEsTFlAG";

conn = remote('localhost',31337);
print(conn.recvline());

m = int(conn.recvline().decode("utf-8").split(" ")[-1].strip());
print(m);
e = 65537;
random.seed(e);

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

def gcd(a,b):
  # Client said the loading screen is too boring
  # So they want something with more flair and movement while they wait
  if(a == 0 or b == 0):
    return "";
  return ".,"[(b // a) & 1] + gcd(b % a,a);

mods = [];
remainders = [];

while len(mods) < 80:
  (conn.recv());
  conn.sendline(b"2");
  s = conn.recvline().strip()[7:];
  currentMod = nextprime(random.randint(1, 100000));
  # print(s);
  (conn.recv());
  conn.sendline(b"haha");
  (conn.recvline());

  # Get the loading first
  exist = {};
  which = {};
  if(currentMod > 10000 or currentMod in mods):
    continue;
  for j in range(currentMod):
    cur = gcd(j,currentMod);
    if(cur in exist):
      exist[cur] += 1;
    else:
      exist[cur] = 1;
      which[cur] = j;

  if(exist[s.decode("utf-8")[1:]] == 1):
    print("YAY " + str(currentMod));
    mods.append(currentMod);
    remainders.append(which[s.decode("utf-8")[1:]]);
  # else:
    # print("REEE " + str(exist[s.decode("utf-8")[1:]]));


phi = (chinese_remainder(mods,remainders));
d = pow(65537,-1,phi);

print(conn.recv());
conn.sendline(b"1");
# print(s);
print(conn.recv());
conn.sendline(str(d).encode("utf-8"));
print(conn.recvline());

# while True:
#   inp = input("Guess Private Key (1) or Encrypt Message (2): ")
#   if (inp == "1"):
#     d = int(input("Enter Private Key: "))
#     print(long_to_bytes(ct, d, n))
#     exit()
    
#   elif (inp == "2"):
#     test_e = e_gen()
#     inp = bytes_to_long(input("Enter Message: ").encode())
#     test_ct = pow(inp, test_e, n)
#     print("Your Message (remember to convert): " + str(test_ct))
    
#   else:
#     print("BAD OPTION")
#     exit()
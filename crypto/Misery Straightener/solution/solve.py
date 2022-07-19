import random;
import math;
import binascii;

def mul(a,b,p):
	assert len(a[0]) == len(b);
	n = len(a);
	uwu = [[0 for _ in range(len(b[0]))] for _ in range(len(a))];
	for k in range(len(a[0])):
		for i in range(len(a)):
			if(a[i][k] == 0):
				continue;
			for j in range(len(b)):
				uwu[i][j] += a[i][k] * b[k][j];
				uwu[i][j] %= p;

	return uwu;

def matExp(mat,e,p):
	print(e);
	assert len(mat) == len(mat[0]);
	if(e == 0):
		return [[(0,1)[i == j] for j in range(len(mat))] for i in range(len(mat))]
	if(e == 1):
		return mat;

	tmp = matExp(mat,e // 2,p);
	print("DONE " + str(e));	
	# print("DONE " + str(len(tmp)) + " " + str(len(tmp[0])));
	if(e & 1):
		return mul(mat,mul(tmp,tmp,2),2);

	return mul(tmp,tmp,2);

class MiseryStraightener:
	def __init__(self):
		random.seed(1337);

		self.bits = 42;
		self.pool = [random.getrandbits(self.bits) for _ in range(13)];
		self.randomConstant = random.getrandbits(self.bits);

	def next(self):
		res = self.pool[-1];
		a = self.pool[12];
		b = self.pool[6];
		c = a ^ b;
		# I can do this just by xor EASY
		c = c ^ (a >> 10);
		# Same thing
		c = c ^ ((b % (1 << 20)) << (self.bits - 20));
		d = (1 << self.bits) - 1 - c;
		e = d;
		if(self.pool[8] & 8):
			e ^= self.randomConstant;

		self.pool.pop();
		self.pool.insert(0,e);
		return res;

	def fastforward(self,x):
		for i in range(x):
			self.next();
		return;

class ms2:
	def __init__(self):
		random.seed(1337);

		self.bits = 42;
		self.pool = [];
		tmp = [random.getrandbits(self.bits) for _ in range(13)];
		for i in range(len(tmp)):
			for j in range(self.bits):
				self.pool.append((tmp[i] >> j) & 1);
		self.pool.append(1);
		tmp = random.getrandbits(self.bits);
		self.randomConstant = [(tmp >> i) & 1 for i in range(self.bits)];

		self.mat = [[0 for j in range(len(self.pool))] for i in range(len(self.pool))];
		for i in range(self.bits * (13 - 1)):
			self.mat[i][i + self.bits] = 1;

		# the 1 node
		self.mat[len(self.mat) - 1][len(self.mat) - 1] = 1;
		for i in range(self.bits):
			self.mat[i + self.bits * 12][i] += 1;
			self.mat[i + self.bits * 12][i] %= 2

			self.mat[i + self.bits * 6][i] += 1;
			self.mat[i + self.bits * 6][i] %= 2

		for i in range(10,self.bits,1):
			self.mat[i + self.bits * 12][i - 10] += 1;
			self.mat[i + self.bits * 12][i - 10] %= 2;

		for i in range(0,20,1):
			self.mat[i + self.bits * 6][i + (self.bits - 20)] += 1;
			self.mat[i + self.bits * 6][i + (self.bits - 20)] %= 2;

		for i in range(self.bits):
			self.mat[len(self.pool) - 1][i] += 1;
			self.mat[len(self.pool) - 1][i] %= 2;

		for i in range(self.bits):
			self.mat[3 + self.bits * 8][i] += self.randomConstant[i];
			self.mat[3 + self.bits * 8][i] %= 2;

	def next(self):
		res = 0;
		# print(self.pool)
		# print(len(self.pool))
		for i in range(self.bits):
			res += self.pool[i + (13 - 1) * self.bits] << i;
		# print(len(self.mat));
		self.pool = mul([self.pool],self.mat,2)[0];
		return res;


	def fastforward(self,x):
		self.pool = mul([self.pool],matExp(self.mat,x,2),2)[0];
		return;


flag = 961324187529262150231144941297949459498043797601643810714360754627060734634014359407613152643271495586117006168448502325284326;

# generator = MiseryStraightener();
generator2 = ms2();

# generator.fastforward(100);
generator2.fastforward(int(1e18));

for i in range(10):
	flag ^= generator2.next() << (i * generator2.bits);

print(binascii.unhexlify(hex(flag)[2:]));

# print(generator.next());
# print(generator2.next());
import random
from mt19937predictor import MT19937Predictor
import binascii

class randomGenerator:
	def __init__(self,generator):
		self.buffer = 0;
		self.bitsLeft = 0;
		self.generator = generator;

	def getRand(self,bits):
		while self.bitsLeft < bits :
			self.buffer = self.buffer | (self.generator.getrandbits(1024) << self.bitsLeft);
			self.bitsLeft += 1024;
		uwu = self.buffer & ((1 << bits) - 1);
		self.buffer = self.buffer >> bits;
		self.bitsLeft -= bits;
		return uwu;

msg = open('output.txt','rb').read().decode("utf-8");
blocks = [];
orz = "ORZ" * 2000;
BLOCK_SIZE = 2;
howmuch = 5600 // BLOCK_SIZE;

for i in range(len(msg) // BLOCK_SIZE):
	blocks.append(msg[i * BLOCK_SIZE:i * BLOCK_SIZE + BLOCK_SIZE]);

for i in range(0,len(blocks) - howmuch):
	print("Trying index " + str(i));
	# try testing if it starts at ith block
	# All 3 orientations as well
	for l in range(1 << (BLOCK_SIZE * 4)):
		# we say rand_{i + k} = k
		uwu = [l];
		for k in range(howmuch - 1):
			cur_uwu = int(blocks[i + k],16);
			next_uwu = int(blocks[i + k + 1],16);
			xor_uwu = cur_uwu ^ next_uwu;
			# = rand_{i + k} ^ rand_{i + k + 1} ^ pt_{i + k + 1}
			pt_ik1 = int(orz[k + 1].encode('utf-8').hex(),16);
			rand_ik1 = xor_uwu ^ pt_ik1 ^ uwu[-1];
			uwu.append(rand_ik1);

		predictor = MT19937Predictor()
		pwp = 8 // BLOCK_SIZE;	

		for k in range(len(uwu) // pwp):
			curRand = 0;
			for l in range(pwp):
				curRand += uwu[pwp * k + l] << (l * BLOCK_SIZE * 4);
			predictor.setrandbits(curRand,32);


		generator = randomGenerator(predictor);

		message = "";
		# ct_{i + howmuch - 1}
		last_ct = int(blocks[i + howmuch - 1],16) ^ uwu[-1];
		for k in range(len(blocks) - i - howmuch):
			cur_uwu = int(blocks[i + howmuch + k],16);
			cur_ct = cur_uwu ^ generator.getRand(BLOCK_SIZE * 4);
			cur_pt = cur_ct ^ last_ct;
			last_ct = cur_ct;
			try:
				message = message + binascii.unhexlify(hex(cur_pt)[2:]).decode('utf-8');
			except:
				message = message;

		if "LITCTF{" in message:
			print("FOUND FLAG! ");
			print(message);
			exit();











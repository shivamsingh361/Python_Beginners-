from os import system,name
from time import sleep

class encript:
	def fun(self, c, d):
		if c.isupper():
			return(chr(65 + (ord(c) - 65 + d)%26))
		elif c.islower():
			return(chr(97 + (ord(c) - 97 + d)%26))
		else:
			return c

	def nuf(self, c, d):
		if c.isupper():
			return chr(90 - (90 - ord(c) + d)%26)
		elif c.islower():
			return chr(122 - (122 - ord(c) + d)%26)
		else:
			return c


	def encode_(self, s, key = 111):
		s1,s2 = '',''
		l = len(s)
		k0  = key % l
		if k0 == 0:
			k0 = 1
		for i in range(l):
			if i + k0 < l:
				s1 += s[i + k0]
			else:
				s1 += s[k0 + i - l]
		k1,k2,k3 = int(str(key)[0]),int(str(key)[1]),int(str(key)[2])
		for j in s1:
			if j.isupper():
				s2 += self.fun(j,k1)
				#k1 -= 1
			elif j.islower():
				s2 += self.fun(j,k2)
				#k2 -= 1
			else:
				s2 += self.fun(j,k3)
				#k3 -= 1
		return(s2)

	def decode_(self, s, key = 111):
		k1,k2,k3 = int(str(key)[0]),int(str(key)[1]),int(str(key)[2])
		s1,s2 = '',''
		for j in s:
			if j.isupper():
				s1 += self.nuf(j,k1)
				#k1 += 1
			elif j.islower():
				s1 += self.nuf(j,k2)
				#k2 += 1
			else:
				s1 += self.nuf(j,k3)
				#k3 += 1
		k0 = len(s)- (key % len(s))
		if k0 == 0:
			k0 = 1
		for i in range(len(s)):
			if i + k0 < len(s):
				s2 += s1[i + k0]
			else:
				s2 += s1[k0 + i - len(s)]
		return(s2)

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


if __name__ == '__main__':
	while 1:
		en = encript()
		clear()
		x = input('Input your choice:\n0.Exit...\n1.Encode a message...\n2.Decode a message...')
		clear()
		if x == '0':
			print('Good to see u! bye.')
			break
		msg = input("Enter message: ")
		key = input("Enter key(3-Digit Integer):")
		sleep(1)
		if not len(key) == 3:
			print('Invalid Input! Try Again.')
		if x == '1':
			print(en.encode_(msg, int(key)))
			sleep(4)
		elif x == '2':
			print(en.decode_(msg, int(key)))
			sleep(4)
		else:
			print('Invalid Input! Try Again.')
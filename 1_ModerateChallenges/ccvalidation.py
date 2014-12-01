import sys

tests = [line for line in open(sys.argv[1], "r").read().splitlines() if line]
for test in tests:
	l = "".join(test.split())
	even = sum(int(x) for x in l[::-2])
	odd = 0
	for i in l[-2::-2]:
		x = int(i)*2
		if x >= 10:
			y = x % 10
			z = x / 10
			odd += y + z
		else:
			odd += x  
	result = odd + even
	if (result % 10 == 0):
		print 1
	else:
		print 0
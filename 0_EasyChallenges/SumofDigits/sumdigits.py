import sys

tests = [line for line in open(sys.argv[1], "r").read().splitlines() if line]
for test in tests:
	s = 0
	x = int(test)
	while x:
		s += x % 10
		x /= 10
	print s
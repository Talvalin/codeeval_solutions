import sys

def main():
	# do something
	tests = [line for line in open(sys.argv[1], "r").read().splitlines() if line]
	output = []

if __name__ == "__main__":
	main()
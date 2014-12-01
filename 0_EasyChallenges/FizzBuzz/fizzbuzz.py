import sys

def fizzbuzz(x, y, n):
    result = []
    for i in range(1, n+1):
        if (i % x == 0) and (i % y == 0):
            result.append("FB")
        elif (i % x == 0):
            result.append("F")
        elif (i % y == 0):
            result.append("B")
        else:
            result.append(i)
    print ' '.join(map(str, result))
    
def main(input):
    # open the input file and read it into a list
    tests = [line for line in open(sys.argv[1], "r").read().splitlines() if line]
    for test in tests:
        l = [int(x) for x in test.split()]
        fizzbuzz(l[0], l[1], l[2])

if __name__ == "__main__":
    main(sys.argv[1])
    
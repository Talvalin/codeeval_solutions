import sys
tests = [line for line in open(sys.argv[1], "r").read().splitlines() if line]

output = []

for t in tests:
    if len(t) <= 55:
        output.append(t)
    else:
        trimmed = t[:40]
    	if trimmed.rfind(' ') != -1:
    		trimmed = trimmed[:trimmed.rfind(' ')]
 	
        trimmed += "... <Read More>"
        output.append(trimmed)

for l in output:
	print l
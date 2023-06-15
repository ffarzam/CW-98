import sys
import os
from collections import Counter


n = len(sys.argv)
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv)

print("\nArguments passed:", end=" ")
if n == 1:
    print("Hello World")
else:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1],"r") as f:
            data=f.read()
            data=data.split()
            print(dict(Counter(data)),"\n")

    else:
        print(sys.argv[1][::-1],"\n")

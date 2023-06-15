import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--size",required=False,action='store_true')
parser.add_argument("path", type=str)

args = parser.parse_args()

for i in os.listdir(args.path):
    if args.size:
        if os.path.isfile(i):
            print(i,", Size: ",os.path.getsize(i)/1024, "KB")
        else:
            print(i)
    else:
        print(i)

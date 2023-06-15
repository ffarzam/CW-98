import argparse


parser = argparse.ArgumentParser()

parser.add_argument("numbers", nargs="*", type=float)

args = parser.parse_args()

print(f"Sum of inputs is {sum(args.numbers)}")
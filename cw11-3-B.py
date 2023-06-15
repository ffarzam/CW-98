from datetime import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("date1", type=str)
parser.add_argument("date2", type=str)

args = parser.parse_args()

date_format = "%Y-%m-%d"
a = datetime.strptime(args.date1, date_format)
b = datetime.strptime(args.date2, date_format)

delta = b - a
print("\033[0;31m"f"The number of days between {args.date1} and {args.date2} is {delta.days} days.""\033[0m")
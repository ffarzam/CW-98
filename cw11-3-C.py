from datetime import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--date", type=str,required=True)
parser.add_argument("--input-format", type=str,required=True)
parser.add_argument("--output-format", type=str,required=True)

args = parser.parse_args()
date_format = datetime.strptime(args.date, args.input_format)
string_format = date_format.strftime(args.output_format)

print("\033[0;31m"f"{string_format}""\033[0m")
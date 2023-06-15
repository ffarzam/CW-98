from datetime import datetime, date, timedelta
import argparse
import logging

logger = logging.getLogger()
f_handler = logging.FileHandler("date_operations.log")
f_format = logging.Formatter('[%(asctime)s] - %(message)s', "%Y-%m-%d %H:%M:%S")
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--mode", type=str,required=True, choices=["add" , "subtract"])
parser.add_argument("--date", type=str,required=True)
parser.add_argument("--days", type=int,required=True)
args = parser.parse_args()


date_ = datetime.strptime(args.date, "%Y-%m-%d").date()

if args.mode == "add":
    result= date_ + timedelta(args.days)
    print("\033[0;31m"f"Result: {result}""\033[0m")
    logger.info(f'MODE: {args.mode} | DATE: {args.date} | DAYS: {args.days} | RESULT: {result}')

elif args.mode == "subtract":
    result = date_ - timedelta(args.days)
    print("\033[0;31m"f"Result: {result}""\033[0m")
    logger.info(f'MODE: {args.mode} | DATE: {args.date} | DAYS: {args.days} | RESULT: {result}')

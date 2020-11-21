import argparse
import sys
def calc(args):
    if args. o=='add':
        return args.x + args.y

    elif args. o=='mul':
        return args.x * args.y

    elif args. o=='sub':
        return args.x - args.y

    elif args. o=='Div':
        return args.x / args.y

    else:
        return "Something went wrong"

    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter first number. Please contact me")

    parser.add_argument('--y', type=float, default=3.0, help="Enter second number.Please contact me")

    parser.add_argument('--o', type=float, default="add", help="Output.Please contact me")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--start", help="first number")
parser.add_argument("--end", help="last number")
args = parser.parse_args()

x = int(args.start or 0)

y = int(args.end or 0)
sum =0
for n in range(x,y+1):
    sum += n
print sum
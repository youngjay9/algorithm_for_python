import sys

line = sys.stdin.readline()

params = line.split(",")

num = int(params[0])

str = params[1]

# if n < 0 or n > 100:
#   return

# if len(l) < 1 or len(l)> 50:
#   return

count = 0
while count < num:
    print(str)
    count += 1

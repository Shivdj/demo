#Program to find whether the given number is even or odd

import sys

args = sys.argv

if(int(args[1]) % 2 == 0):
    print('Given number is even')
else:
    print('Given number is odd')
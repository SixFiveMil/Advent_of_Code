#read input file in directory where the script is saved at
import os
r = 0
with open('2015\Day 1\input.txt', 'r') as f:
    for x in str(f.readlines()):
        print(x)
        if x == "(":
            r+=1
        elif x== ")":
            r-=1

print(r)

#read input file in directory where the script is saved at
import os
r = 0
p = 0
with open('2015\Day 1\input.txt', 'r') as f:
    for x in str(f.readlines()):
#find char position when r = -1

        #print(x)
        if r == -1:
            continue
        if x == "(":
            r+=1
            p+=1
        elif x== ")":
            r-=1
            p+=1

print(r, p)


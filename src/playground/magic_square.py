#!/usr/bin/env python3
# encoding= utf-8

""" This module is to get the birthday date as input in dd mm yy yy format and generate magic square.

Magic Squares, where patterns of numbers arranged in a square produce the same total when added diagonally,
horizontally, vertically and often in the corners and central square.

"""

name = input("Enter your name:")
r1 = []
r1.insert(0,int(input("Enter your date of birth in DD format:"))) 
r1.insert(1,int(input("Enter your month of birth in MM format:")))
r1.insert(2,int(input("Enter your year of birth first two digit:")))
r1.insert(3,int(input("Enter your year of birth last two digit:")))

# Caluculating Magic Square
r2 = [r1[3]+1, r1[2]-1,r1[1]-3,r1[0]+3]
r3 = [r1[1]-2, r1[0]+2,r1[3]+2,r1[2]-2]
r4 = [r1[2]+1, r1[3]-1,r1[0]+1,r1[1]-1]

print("\n Hey "+name +"! You're Birthday Magic Square is:\n")
print(r1)
print(r2)
print(r3)
print(r4)
print("\n")
print("Magic Squares, where patterns of numbers arranged in a square produce the same total when added diagonally,horizontally, vertically and often in the corners and central square.\n")





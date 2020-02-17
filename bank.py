
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:02:03 2020

@author: Tamil"""
print("Welcome to bank")
n=1
amt=10000
def deposit(amt,add):
    amt+=add
    print(amt)
def drew(amt,sub):
    amt-=sub
    print(amt)
yes=['deposit','Deposit','DEPOSIT','d','D']
no=['Withdrew','withdrew','WITHDREW','w','W']
while(n==1):
    response=input('What service would you like to have?')
    if response in yes:
        add=int(input("enter the amount to deposit"))
        deposit(amt,add)
        break
    elif response in no:
        sub=int(input("enter the amount to withdrew"))
        drew(amt,sub)
        break
print(amt)
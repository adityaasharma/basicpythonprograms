# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:13:16 2019

@author: adity
"""
A=[(x) for x in input().split()] #reading whole list as a string element in a list
A=A[0] #picking the first element of the list, i.e. the input
A=A[1:] #selecting everything except the first'[' square bracket
A=A[:len(A)-1] #selecting everything except the last ']' bracket
A=A.split(',') #now splitting the whole values by ','
A=list(map(int, A)) #mapping each value as an int intot he same list. List is ready now for the logic

def leastmissingpositiveinteger(A):
    A=sorted(A)
    for i in range(1,A[len(A)-1]+2):
        if i not in A:
            return (i)
            break

print (leastmissingpositiveinteger(A))
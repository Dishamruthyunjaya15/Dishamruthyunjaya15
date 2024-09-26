# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:42:08 2024

@author: SPURGE
"""

def find_equilibrium_position(N, A):
    total_sum = sum(A)  
    left_sum = 0  

    for i in range(N):
        right_sum = total_sum - left_sum - A[i]
        
        if left_sum == right_sum:
            return i + 1  

        left_sum += A[i]

    return "NOT FOUND"

# Input reading
N = int(input())
A = list(map(int, input().split()))
result = find_equilibrium_position(N, A)
print(result)
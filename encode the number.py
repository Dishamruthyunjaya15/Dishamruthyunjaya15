# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:41:33 2024

@author: SPURGE
"""

def encode_number(N):
    str_N = str(N)
    encoded_str = ""
    
    for digit in str_N:
        squared_digit = int(digit) ** 2  # Square the digit
        encoded_str += str(squared_digit)  
    
    encoded_value = int(encoded_str)
    
    return encoded_value

# Input reading
N = int(input())

result = encode_number(N)
print(result)
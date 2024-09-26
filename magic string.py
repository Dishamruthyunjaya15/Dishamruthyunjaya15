# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:40:22 2024

@author: SPURGE
"""

from collections import Counter

def min_steps_to_magic_string(S):
    if len(set(S)) == 1:
        return 0
    
    freq = Counter(S)
    
    max_freq = max(freq.values())
    
    return len(S) - max_freq

S = input()

result = min_steps_to_magic_string(S)
print(result)
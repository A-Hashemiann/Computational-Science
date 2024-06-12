#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:17:50 2024

@author: amen
"""

def dec_bin(n):
    """
    converting an integer to a binary string
    
    parameters:
    n (int): The integer to convert
    
    returns:
    str: The binary representation of the integer with '0b' prefix.
    """
    if n == 0:
        return '0b0'
    
    is_negative = n < 0
    n = abs(n)
    
    binary_digits = []
    
    while n > 0:
        binary_digits.append(str(n % 2))
        n = n // 2
    
    # reverse the list of digits to get the correct binary representation
    binary_digits.reverse()
    
    binary_str = ''.join(binary_digits)
    
    if is_negative:
        return '-0b' + binary_str
    else:
        return '0b' + binary_str

# Example usage
positive_num = 30
negative_num = -10

print(f"The binary representation of {positive_num} is: {dec_bin(positive_num)}")
print(f"The binary representation of {negative_num} is: {dec_bin(negative_num)}")
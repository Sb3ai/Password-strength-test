# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:41:55 2026

@author: bu3li
"""

def user_input():
    point = 0
    Password = input("Please enter a password >> ")
    
    # We check the length of the password here.
    if len(Password) >= 8 and len(Password) <= 64:
        point += 1
    
    return point


fetch_points = user_input()
print(fetch_points)
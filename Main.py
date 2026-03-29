# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:41:55 2026

@author: bu3li
"""

def user_input():
    point = 0
    symbols = ["!","@","#","$","%","^","&","*","()","_","-","+","~","`","'",".","/",";","(","[","]","/",">","<"]
    Password = input("Please enter a password >> ")
    
    # We check the length of the password here.
    if len(Password) >= 8 and len(Password) <= 64:
        point += 1
    
    
    # Here we implemented a system that see's the list of symbols to detect wether if their are symbols in the password
    # Hence increasing the strength point
    for sym in symbols:
        if sym in Password:
            point += 1
            break
    return point


fetch_points = user_input()
print(fetch_points)
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:41:55 2026

@author: bu3li
"""
"""
def user_input():
    point = 0
    symbols = ["!","@","#","$","%","^","&","*","()","_","-","+","~","`","'",".","/",";","(","[","]","/",">","<"]
    Password = input("Please enter a password >> ")
    
    # We check the length of the password here.
    if len(Password) >= 8 and len(Password) <= 64:
        point += 1
    
    if len(Password) >= 12 and len(Password) <= 64: # This is a bonus point, if the password is longer than or equal to 12 then extra points
        point += 1
    
    for letter in Password:
        if letter.isupper(): # Here we detect if the password contains Capitalized words
            print(letter)
            point += 1
            break
    for i in Password:
        if i.isdigit(): # Here we detect if a the password contains any integar inside the password. if so point ++ 1
            point += 1
            break
    # Here we implemented a system that see's the list of symbols to detect wether if their are symbols in the password
    # Hence increasing the strength point
    for sym in symbols:
        if sym in Password:
            point += 1
            break
    return point


fetch_points = user_input()
print(fetch_points)
"""

class Password_Checker:
    def __init__(obj, password, point=0):
        obj.password = password
        obj.symbols = ["!","@","#","$","%","^","&","*","()","_","-","+","~","`","'",".","/",";","(","[","]","/",">","<"]
        obj.point = point
    
    def checkLen(obj):
        if len(obj.password) >= 8 and len(obj.password) <= 64:
            obj.point += 1
        if len(obj.password) >= 12 and len(obj.password) <= 64:
            obj.point += 1
    
    def checkLetters(obj):
        for letter in obj.password:
            if letter.isupper():
                obj.point += 1
                break
    def checkNums(obj):
        for number in obj.password:
            if number.isdigit():
                obj.point += 1
                break
                
    def checkSym(obj):
        for letter in obj.password:
            if letter in obj.symbols:
                obj.point += 1
                break
    def __str__(obj):
        obj.checkLen()
        obj.checkLetters()
        obj.checkNums()
        obj.checkSym()
        print(f"The password {obj.password} strength is [{obj.point}/5]")
        if obj.point <= 2:
            print("Your password is considered weak.")
        elif obj.point <= 3:
            print("Your password is conisdered good")
        elif obj.point <= 4:
            print("Your password is strong and good.")
    

user_input = input("Enter your password >> ")

user = Password_Checker(user_input)
user.__str__()
            
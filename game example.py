# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 09:26:26 2026

@author: SOORYA
"""

import random                                                                
secrect_number=random.randint(1,20)
class Guessnumber:
    def __init__(self):
        secrect_number=random.randint(1,20)
        self.secrect_number=secrect_number
        
    def guess_number(self):
            predict_number=int(input("enter a number"))
            if predict_number<self.secrect_number:
                print("predict_number is less than secrect_number")
            elif predict_number>self.secrect_number:
                print("predict_number is greater than secrect_number")
            else:
                print("correct number")
randomnumber=Guessnumber() 
randomnumber.guess_number()      


import random
secrect_number=random.randint(1,10)
class Guessnumber:
    def __init__(self):
        secrect_number=random.randint(1,10)
        self.secrect_number=secrect_number
    def guess_number(self):
        while True :
            predict_number=int(input("enter a number"))
            if  predict_number==secrect_number:
                 print("equel number")
                 break
            elif predict_number<self.secrect_number:
                print("predict_number is less than secrect_number")
            else:
                print("predict_number is greater than secrect_number")
            
                      
                    
randomnumber=Guessnumber() 
randomnumber.guess_number()      

import random
dies_number=random.randint(1,6)
class Diesnumber:
    def __init__(self):
        dies_number=random.randint(1,6)
        self.dies_number=dies_number          
    def predict_number(self):
        while True:
            guess_number=int(input("enter a number"))
            if dies_number==guess_number:
                print("two numbers are equel")
                break
            else:
                print("two numbers are not equel")

samenumber=Diesnumber()
samenumber.predict_number()


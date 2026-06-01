# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 21:11:56 2026

@author: SOORYA
"""

class Calculater:
    def __init__(self):
        self.a=None
        self.b=None
        self.operation=None
    def summ_number(self):
        print("sum of the numbers")
        return self.a+self.b
    def subtract_number(self):
        print("subtract value of two numbers")
        return self.a-self.b
    def multiple_number(self):
        print("multiple of two numbers")
        return self.a*self.b
    def divition_number(self):
        if self.b!=0:
            
            print("divition of two numbers")
            return self.a/self.b
        else:
            print("not valid this function")
         
    
def arithmetic_function():
        obj1=Calculater()
        obj1.a=int(input("enter a number:"))
        obj1.operation=input("enter operation(+,-,*,/):")
        obj1.b=int(input("enter a number:"))
        #result = ("operation"),(self.a,self.b)
        if obj1.operation=="+":
            print(obj1.summ_number())
        elif obj1.operation=="-":
            print(obj1.subtract_number())
        elif obj1.operation=="*":
            print(obj1.multiple_number())
        elif obj1.operation=="/":
            print(obj1.divition_number())
        else:
            print("invalid")
       
           
arithmetic_function()







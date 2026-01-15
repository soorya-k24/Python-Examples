# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 09:22:31 2026

@author: SOORYA
"""

class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def calculate_emp_salary (self,salary,hours_worked):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amount=(overtime*(salary/50))
            return salary+overtime_amount
        else:
            return salary 
    def emp_assign_department(self,new_department):
        self.emp_department=new_department
    def print_employee_details(self): 
        print( self.emp_id, self.emp_name, self.emp_salary, self.emp_department)
ADAMS=Employee("E7676","ADAMS",50000,"ACCOUNTING")
ADAMS.calculate_emp_salary(50000,80)            
ADAMS.emp_assign_department("HR")
ADAMS.print_employee_details()   
class Bankaccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposit(self,amount):
         if amount>0:
             self.balance+=amount
             return self.balance
         else:
             print( "amount should be positive") 
    def withdrow(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return self.balance
        else:
           print("insufficient balance")
    def check_bankbalance(self):
        print(self.balance)
john=Bankaccount(17564367813,5030,"1/12/2025","john")   
john.deposit(100)
john.withdrow(60)             
john.check_bankbalance()    
class Inventory:
    def __init__(self):
        self.item_detail={}
    def add_item(self,item_id,item_name,stock_count,price):
        self.item_detail[item_id]={"item_name":item_name,"stock_count":stock_count,"price":price}
    def update_item(self,stock_count,itme_id):
        self.item_detail[itme_id]["stock_count"]=stock_count
    def check_item_details(self):
        print(self.item_detail)
veg=Inventory()
veg.add_item(1234,"tomato",16,100)
veg.update_item(10,1234) 
veg.check_item_details()


















   

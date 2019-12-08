# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:35:28 2019

@author: sebst
"""


import pandas as pd
import sys
import datetime

def read_bills():
    ### Note : there should be no duplicates in the data so drop duplicates has been used
   return((pd.read_csv("bills.csv", names = ['company', 'customer', 'year', 'month', 'day', 'amount', 'credit/debit'], header = None).drop_duplicates()))
    

def enter_provider(p_df):
    while True:
        new_company = input("Enter provider : ")
        if len(p_df[p_df['company'].str.strip() == new_company]) != 0:    
            break
    return(new_company)

def enter_customer(p_df):
    while True:
        new_customer = input("Enter customer : ")
        if len(p_df[p_df['customer'].str.strip() == new_customer]) != 0:
            return(new_customer)

        while True:
            add_customer = input("Unknown Customer - Add new customer [Y/N] : ")
            if add_customer.upper() == "Y" or add_customer.upper() == "N":
                break
            
        if add_customer.upper() == "Y":
            return(new_customer)
 
def enter_date():
    while True:
        date_entry = input('Enter a date in YYYY-MM-DD format : ')
        try:
            year, month, day = map(int, date_entry.split('-'))
            date1 = datetime.date(year, month, day)
            break
        except:
            print("Error")
    return(date1)
    

def enter_amount():
    while True:
        number_entry = input("Enter Amount [-ve indicates payment] : ")
        try:
            val_number_entry = float(number_entry)
            break
        except:
            print("Enter valid number ")
            
    return(round(val_number_entry,2))
            

           
def enter_new_trans():
    new_company = enter_provider(df)
    new_customer = enter_customer(df)
    new_date = enter_date()
    new_amount = enter_amount()
    print("Company : " + new_company + "   Customer : " + new_customer + "    Date : " + str(new_date) + "     Amount : " + str(new_amount))
    print(new_amount)
    print(new_date.year)
    print(new_date.month)
    print(new_date.day)     
    if new_amount < 0:
        new_cr_db = 'credit'
        new_amount = new_amount * -1
    else:
        new_cr_db = 'debit'
    objdf = df.append({'company' : new_company, 'customer' : new_customer, 'year' : new_date.year, 'month' : new_date.month, 'day' : new_date.day, 'amount' : new_amount, 'credit/debit' : new_cr_db}, ignore_index = True)      
    print(objdf)
                

    
    
df = read_bills()
enter_new_trans()


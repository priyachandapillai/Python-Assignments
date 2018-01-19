#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:59:34 2017

@author: PriyaChandapillai
"""

print("Welcome to Cafe ABC")
discount, total_bill=0.0,0.0
while(True):
    choice=int(input("Enter your option: 1. Generate Bill 2.Exit"))
    if (choice==1):
        coupon_status=input("Do you have coupon(Y/N)?")
        if (coupon_status=="Y"):
            discount=float(input("Enter amount of coupon:- "))
        no_of_person=int(input("Enter number of persons:- "))
        for i in range(1,no_of_person+1):
            starter_price=float(input("Enter person " +str(i) + " starter_price:- "))
            meal_price=float(input("Enter person " +str(i) + " meal_price:- "))
            dessert_price=float(input("Enter person " +str(i) + " dessert_price:- "))
            print("Total Bill of person" +str(i) +" is:- "+str(starter_price+meal_price+dessert_price))
            total_bill+=starter_price+meal_price+dessert_price
        print("Total bill of " +str(no_of_person)+" is:" +str(total_bill-discount))
        discount=0.0
    else:            
        print("GoodBye")
        break

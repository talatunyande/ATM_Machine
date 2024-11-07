#!/usr/bin/python3
balance=1000
deposited_fund=float(input("Input deposit amount :"))
total_deposits=0
if deposited_fund >0:
                total_deposits+=deposited_fund
                print(f"you have deposited ${deposited_fund}. Your new balance is ${balance}")
else:
                print("please enter a positive number .")
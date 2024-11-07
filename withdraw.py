#!/usr/bin/python3
balance=1000
total_withdrawals =0
amount_withdrawn = float(input("input amount to withdraw : "))
if amount_withdrawn >0:
                if balance !=amount_withdrawn:
                    total_withdrawals +=amount_withdrawn
                    print (f"you have withdrawn ${amount_withdrawn}.new balance is: ${balance}")
#!/usr/bin/python3
# assigning a variable balance to 1000
balance=(1000)
#assigning number to variable number_of_attempt_allowed

import user_pin
user_pin.number_of_attempt_allowed

    #requesting user input of pin
 

total_deposits =0
total_withdrawals =0
        #using whileTrue to loop to display the main menu
while True:
        print("\n--- Main_Menu---")
        print("\n 1.Check Balance","\n 2.Deposit Funds","\n 3.withdraw Funds","\n 4.Change Pin","\n 5. Exist")

        #using If,else,elif statements for cjecking balance,depositingfunds,changing pin and existing
        Option=int(input("select Options (1-5):"))
        if Option==1:
            print(f"you have ${balance} left")
        elif Option==2:
            import deposited
            deposited.deposited_fund
            
        elif Option==3:
            import withdraw
            withdraw.amount_withdrawn
                               
        elif Option==4:
                   import new_pin
                   new_pin.new_pin 
                    
        elif Option==5:
                        print(f"total withdrawal is :${total_withdrawals} and total deposit made is ${total_deposits}\n total amount is ${balance}")
                        break
        else:
                        print("invalid option, please try again")





        